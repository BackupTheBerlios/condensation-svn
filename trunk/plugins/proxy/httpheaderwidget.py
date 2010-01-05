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

class HTTPHeaderWidget(gtk.VBox):

    def __init__(self):
        gtk.VBox.__init__(self)

        self.liststore = gtk.ListStore(str, str)
        self.treeview = gtk.TreeView(self.liststore)

        self.column_name = gtk.TreeViewColumn(_('Name'))
        self.treeview.append_column(self.column_name)
        self.cell_name = gtk.CellRendererText()
        self.column_name.pack_start(self.cell_name, True)
        self.column_name.add_attribute(self.cell_name, 'text', 0)

        self.column_value = gtk.TreeViewColumn(_('Value'))
        self.treeview.append_column(self.column_value)
        self.cell_value = gtk.CellRendererText()
        self.column_value.pack_start(self.cell_value, True)
        self.column_value.add_attribute(self.cell_value, 'text', 1)

        self.add(self.treeview)
        self.show_all()


    def set_headers(self, headers):
        self.liststore.clear()
        keys = headers.keys()
        keys.sort()
        for key in keys:
            self.liststore.append((key, headers[key]))

