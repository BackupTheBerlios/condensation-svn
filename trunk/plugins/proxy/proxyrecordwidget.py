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

import gtk

from httpheaderwidget import HTTPHeaderWidget

class ProxyRecordWidget(gtk.VBox):

    def __init__(self):
        gtk.VBox.__init__(self)

        # request header
        expander = gtk.Expander(_('Request Header'))
        self.request_header_widget = HTTPHeaderWidget()
        expander.add(self.request_header_widget)
        self.pack_start(expander, False, True)
        expander.show_all()
        # request Body
        expander = gtk.Expander(_('Request Body'))
        expander.add(gtk.Label('PLACEHOLDER'))
        self.pack_start(expander, False, True)
        expander.show_all()
        # response header
        expander = gtk.Expander(_('Response Header'))
        self.response_header_widget = HTTPHeaderWidget()
        expander.add(self.response_header_widget)
        self.pack_start(expander, False, True)
        expander.show_all()
        # response body
        expander = gtk.Expander(_('Response Body'))
        expander.add(gtk.Label('PLACEHOLDER'))
        self.pack_start(expander, False, True)
        expander.show_all()



    def set_record(self, record):
        if hasattr(record, 'request_headers'):
            self.request_header_widget.set_headers(record.request_headers)
        if hasattr(record, 'response_headers'):
            self.response_header_widget.set_headers(record.response_headers)




