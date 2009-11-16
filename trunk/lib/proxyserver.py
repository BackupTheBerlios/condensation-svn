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

import lib.core

from proxyrequesthandler import ProxyRequestHandler


class ProxyServer(lib.core.CONBorg):

    _attribute_definitions = (
        {'name': 'ports', 'type': 'integer[]', 'default': (8000,), 'min':1, 'max': 65535},
    )
    _signal_list = (())


    class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer): pass


    def __init__(self):
        lib.core.CONBorg.__init__(self)
        self._logger = logging.getLogger("proxy")



    def restart(self):
        self._logger.info("Starting proxy ...")


