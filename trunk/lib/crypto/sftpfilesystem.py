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

import logging

import lib.core

class SFTPFileSystem(lib.core.FileSystem):


    def __init__(self, paramiko_transport):
        """
        """
        self.path_separator = '/'
        self._logger = logging.getLogger('da.dasftpfilesystem')
        self.sftp_client = paramiko_transport.open_sftp_client()



    def listdir(self, path):
        """
        """
        realpath = self.construct_path(path)
        self._logger.debug("SFTP-FS : listdir %s" % realpath)
        return self.sftp_client.listdir(realpath)



    def mkdir(self, path):
        """
        """
        realpath = self.construct_path(path)
        self._logger.debug("SFTP-FS : mkdir %s" % realpath)
        return self.sftp_client.mkdir(realpath)



    def open(self, mode, path):
        """
        """
        realpath = self.construct_path(path)
        self._logger.debug("SFTP-FS : open %s" % realpath)
        return self.sftp_client.open(realpath, mode)


    def destroy(self):
        self.sftp_client.close()

