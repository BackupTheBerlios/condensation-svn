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

import BaseHTTPServer
import SocketServer
import logging
import threading
import select

import lib.core

from proxyrequesthandler import ProxyRequestHandler


class ProxyServer(lib.core.CONBorg):

    _attribute_definitions = (
        {'name': 'ports', 'type': 'integer[]', 'default': (8000,), 'min':1, 'max': 65535},
    )
    _signal_list = (())

    _running_servers = {}
    _running_server_threads = {}

    # need to implement serve_forever() and shutdown(), because python2.5 has no shutdown()
    class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):

        def serve_forever(self, poll_interval=0.5):
            self.__running = True
            while self.__running:
                r, w, e = select.select([self], [], [], poll_interval)
                if r:
                    self._handle_request_noblock()


        def shutdown(self):
            self.__running = False



    def __init__(self):
        lib.core.CONBorg.__init__(self)



    def start(self):
        if self._running_servers:
            raise Exception("Servers are still running, stop them first")
        # start one server for each port
        for port in self.ports:
            logging.getLogger("proxy").info("starting proxy on port %d" % port)
            server = self.ThreadedHTTPServer(('127.0.0.1', port), ProxyRequestHandler)
            name = "proxy%d" % port
            thread = threading.Thread(target=server.serve_forever, name=name)
            thread.daemon = True
            thread.start()
            self._running_servers[port] = server
            self._running_server_threads[port] = thread
        # check if they are running
        for port, thread in self._running_server_threads.iteritems():
            if thread.isAlive():
                logging.getLogger("proxy").info("proxy on port %d is running" % port)
            else:
                logging.getLogger("proxy").error("proxy on port %d is NOT running" % port)



    def stop(self):
        if self._running_servers:
            # signal all server threads to stop
            for port in self._running_servers.keys():
                logging.getLogger("proxy").info("stopping proxy on port %d" % port)
                server = self._running_servers[port]
                server.shutdown()
                del self._running_servers[port]
            # now wait until they have done so
            for port in self._running_server_threads.keys():
                thread = self._running_server_threads[port]
                thread.join()
                del self._running_server_threads[port]
                logging.getLogger("proxy").info("proxy on port %d stopped" % port)

