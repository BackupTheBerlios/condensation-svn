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

import condensation.core


class ProxyRecord(object):
    """represents a proxy record, ie. one request and it's associated data."""



class ProxyRecordList(condensation.core.CONObject):
    """List of ProxyRecords."""

    _attribute_definitions = [
    ]
    _signal_list = ('record-added',)


    def __init__(self):
        condensation.core.CONObject.__init__(self)
        self._list = []



    def add_request(self, handler_object):
        #print dir(handler_object)
        record = ProxyRecord()
        record.client_address = handler_object.client_address
        record.request_type = handler_object.command
        record.path = handler_object.path
        record.version = handler_object.request_version

        #TODO: headers

        self._list.append(record)
        self.raise_signal('record-added', record)


