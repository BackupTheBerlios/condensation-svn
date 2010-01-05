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

import SocketServer
import select
import socket
import urlparse
import re
import mimetools


class ProxyRequestHandler(SocketServer.BaseRequestHandler):

    server_version = "Condensation Proxy"
    rbufsize = 0                        # self.rfile Be unbuffered

    mapping_table = {}
    map_all = None

    proxyrecordlist = None

    re_request_line = re.compile('(?P<method>\w+) (?P<uri>[^ ]+) HTTP/(?P<http_version>[0-9]+\.[0-9]+)\r\n')

    message_class = mimetools.Message


    @classmethod
    def add_mapping(cls, original_domain, new_domain, new_port):
        cls.mapping_table[original_domain] = (new_domain, new_port)



    def _map(self, netloc):
        if self.map_all:
            return self.map_all

        if netloc[0] in self.mapping_table:
            return self.mapping_table[netloc[0]]

        dom = netloc[0].split('.')
        while dom:
            wc = '*.' + '.'.join(dom)
            if wc in self.mapping_table:
                return self.mapping_table[wc]
            dom.pop(0)

        return netloc


    def handle(self):
        self.c_file = self.request.makefile()
        line = self.c_file.readline()
        m = self.re_request_line.match(line)
        if not m:
            # TODO: handle this better
            self.request.close()
            print "ERROR - could not parse request-line"
            return
        print m.groups()
        self.record = self.proxyrecordlist.new_record()
        self.record.method = m.group('method')
        self.record.uri = m.group('uri')
        self.record.http_version = m.group('http_version')
        self.headers = dict(self.message_class(self.c_file, 0))
        self.record.request_headers = self.headers




