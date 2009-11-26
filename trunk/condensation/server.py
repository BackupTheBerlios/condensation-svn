############################################################################
#    Copyright (C) 2009 by Thomas Hille                                    #
#    thomas.hille@nightsabers.org                                          #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################


import xml.etree.ElementTree as ET
import os
import paramiko
import logging
import md5
import socket

import condensation.crypto
import condensation.core

from vhost import VHost

class Server(condensation.core.CONObject):
    """
    A (remote) apache installation including several VHosts.
    """

    _attribute_definitions = [
        {'name': 'name', 'type': 'string', 'default': 'no name'},
        {'name': 'host', 'type': 'string', 'default': 'example.com'},
        {'name': 'ssh_port', 'type': 'string', 'default': '22'},
        {'name': 'ssh_user', 'type': 'string', 'default': 'root'},
        {'name': 'ssh_user_home', 'type': 'string', 'default': '/root'},
        {'name': 'ssh_key_fingerprint', 'type': 'string', 'default': ''},
        {'name': 'ssh_autoconnect', 'type': 'boolean', 'default': False},
        {'name': 'apache_base', 'type': 'string', 'default': '/var/www'},
        {'name': 'apache_confbase', 'type': 'string', 'default': '/etc/apache2'},
        {'name': 'apache_available', 'type': 'string', 'default': '/etc/apache2/servers-available'},
        {'name': 'apache_enabled', 'type': 'string', 'default': '/etc/apache2/servers-enabled'},
        {'name': 'apache_user', 'type': 'string', 'default': 'www-data'},
        {'name': 'apache_group', 'type': 'string', 'default': 'www-data'},
        {'name': 'drupal_cronfile', 'type': 'string', 'default': '/etc/cron.hourly/drupal'},
        {'name': 'mysql_host', 'type': 'string', 'default': 'localhost'},
        {'name': 'mysql_user', 'type': 'string', 'default': 'root'},
        {'name': 'mysql_password', 'type': 'string', 'default': ''},
        {'name': 'vhosts', 'type': 'VHost[]', 'default': [], 'navigatable': True},
    ]

    _signal_list = ('ask-password', 'changed', 'unknown-key', 'connected', 'disconnected')

    servers = [] #: list of all Server objects


    def __init__(self):
        """
        Your standard init, calls `condensation.core.CONObject.__init__()`.

        Registers the signals 'ask-password', 'changed' and 'unknown-key'.
        """
        condensation.core.CONObject.__init__(self)

        # get us a logger
        self._logger = logging.getLogger('server')

        # add to gloabl list of servers
        self.servers.append(self)

        #self.vhosts = {} #: list of vhosts
        self._sftpfs = None #: a DASFTPFileSystem object
        self._transport = None #: paramiko transport object
        self._transport_live = False #: transport status

        self._ssh_password = None #: the password used by ssh for authentification



    def delete(self):
        """
        Remove server from the global list of servers.
        """
        self.servers.remove(self)



    def add_vhost(self, vhost):
        """
        Adds a vhost to the server and raises a 'changed' signal.

        :param vhost: the `VHost` object
        """
        self.vhosts.append(vhost)
        vhost._server = self
        self.raise_signal("changed")



    def wakeup(self):
        for vhost in self.vhosts:
            vhost._server = self


    #
    # Connection stuff
    #
    def connect_to_server(self):
        """
        Connect to the server.

        Raises a 'ask-password' signal, when no password is given.
        """
        if not self._transport_live:
            keymanager = condensation.crypto.KeyManager()

            self._logger.info("%s : connecting" % self.host)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, int(self.ssh_port)))

            self._logger.info("%s : opening transport" % self.host)
            self._transport = paramiko.Transport(sock)
            self._transport.start_client()

            fingerprint = md5.new(str(self._transport.get_remote_server_key())).hexdigest()
            if not self.ssh_key_fingerprint:
                self._logger.warning("%s : no known fingerprint" % self.host)
                self.raise_signal("unknown-key", fingerprint)
                # TODO: respect 'cancel' (ie catch exception from daserverwidgets)
            else:
                if self.ssh_key_fingerprint != fingerprint:
                    raise Exception("%s : presented key has wrong fingerprint (is %s expected %s" % (self.host,fingerprint,self.ssh_key_fingerprint))
            self._logger.info("%s : Fingerprint matches" % self.host)

            try: # Try public key authentication
                self._transport.auth_publickey(
                    self.ssh_user,
                    keymanager.get_ssh_auth_key()._key)
            except (paramiko.BadAuthenticationType, paramiko.AuthenticationException), e:
                if isinstance(e, paramiko.BadAuthenticationType):
                    self._logger.warning("%s : public key authentication not supported" % self.host)
                elif isinstance(e, paramiko.AuthenticationException):
                    self._logger.warning("%s : public key authentication FAILED (is the key installed on the server?)" % self.host)
                else:
                    self._logger.error("something strange happened")
                    raise e
                # Try password authentication
                self._logger.info("%s : trying password based authentication" % self.host)
                while 1: # Try until the user provides the right password
                    self.raise_signal('ask-password') # get us a password
                    try:
                        self._transport.auth_password(username=self.ssh_user, password=self._ssh_password, fallback=True)
                    except Exception, e:
                        if isinstance(e, paramiko.BadAuthenticationType):
                            self._logger.warning("%s : password authentication not supported" % self.host)
                            self._transport.close()
                            self._logger.warning("%s : Giving up..." % self.host)
                            return
                        elif isinstance(e, paramiko.AuthenticationException):
                            self._logger.warning("%s : password authentication FAILED (probably wrong password)" % self.host)
                        else:
                            self._logger.error("something strange happened")
                            raise e
                    else:
                        break # it worked .....

            self._logger.info("authenticated connection to server %s" % self.host)
            self._transport_live = True
            self._post_connect()
            self.raise_signal("connected")



    def _post_connect(self):
        """
        Called after a transport is established and authentication took place.
        """
        fs = self.get_sftp_filesystem()
        for vhname in fs.listdir(self.apache_available):
            vhost = VHost()
            vhost.name = vhname
            self.add_vhost(vhost)
            vhost.read_config()



    def disconnect(self):
        """
        Disconnect from the server.

        Removes all vhosts and raises a 'changed' signal.
        """
        if self._sftpfs != None:
            self._sftpfs.destroy()
            self._sftpfs = None
        # Close the SSH Transport.
        if self._transport_live:
            self._logger.info("Closing Transport to %s" % self.host)
            self._transport.close()
            self._transport_live = False
            self._logger.info("closed")
        self.raise_signal("disconnected")



    def get_connected(self):
        """
        Returns wether the connection is live or not.

        The SFTP connection is not taken into account, just the transport.
        """
        return self._transport_live



    def get_sftp_filesystem(self):
        """
        Open a SFTP connection and returns a `condensation.crypto.SFTPFileSystem`.
        """
        self.connect_to_server()
        if self._sftpfs == None:
            self._sftpfs = condensation.crypto.SFTPFileSystem(self._transport)
            self._sftpfs.home_dir = self.ssh_user_home
        return self._sftpfs



    def install_auth_key(self):
        self._logger.info("%s : installing public key for authentication" % self.host)
        if '.ssh' not in self._sftpfs.listdir('~'):
            self._logger.debug("%s : creating ~/.ssh directory" % self.host)
            self._sftpfs.mkdir('~/.ssh')
        self._logger.debug("%s : adding key to ~/.ssh/authorized_keys" % self.host)
        file = self._sftpfs.open('a', '~/.ssh/authorized_keys')
        key = DAKeyManager().get_ssh_auth_key()
        file.write(key.get_authorized_keys_line())
        file.close()
        self._logger.debug("%s : installed key" % self.host)



condensation.core.CONObject.register_attribute_type('Server', Server.object_serializer, Server.object_deserializer)
