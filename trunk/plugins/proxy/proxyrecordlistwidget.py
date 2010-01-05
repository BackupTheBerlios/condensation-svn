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

import gobject
import gtk

import condensation

class ProxyRecordListWidget(gtk.ScrolledWindow):
    """
    Widget used for editing a list of integers
    """

    def __init__(self, proxy):
        gtk.ScrolledWindow.__init__(self)
        self.proxy = proxy

        self.liststore = gtk.ListStore(object)
        self.treeview = gtk.TreeView(self.liststore)

        self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.set_property('shadow-type', gtk.SHADOW_IN)
        self.add(self.treeview)

        # client column
        self.column_client = gtk.TreeViewColumn(_('Client'))
        self.treeview.append_column(self.column_client)
        self.cell_client = gtk.CellRendererText()
        self.column_client.pack_start(self.cell_client, True)
        self.column_client.set_cell_data_func(self.cell_client, self._cell_data_client)
        self.column_client.set_property('resizable', True)

        # add some columns
        self._add_column_str(_('Method'), 'method')
        self._add_column_str(_('URI'), 'uri')

        # general treeview stuff
        self.treeview.set_reorderable(False)
        self.treeview.set_headers_visible(True)
        self.treeview.set_rules_hint(True)
        self.treeview.get_selection().set_mode(gtk.SELECTION_SINGLE)
        self.treeview.connect("cursor_changed", self._cursor_changed)

        self.show_all()

        self.recordlist = self.proxy.get_recordlist()
        for record in self.recordlist._list:
            self.liststore.append((record,))

        self.recordlist.connect_signal('record-added', self._record_added)



    def _add_column_str(self, name, attrib):
        column = gtk.TreeViewColumn(name)
        self.treeview.append_column(column)
        cell = gtk.CellRendererText()
        column.pack_start(cell, True)
        column.set_cell_data_func(cell, self._cell_data_str, attrib)
        column.set_property('resizable', True)



    def _record_added(self, recordlist, record):
        self.liststore.append((record,))



    def _cell_data_client(self, column, cell_renderer, tree_model, iter):
        record = tree_model.get_value(iter, 0)
        if hasattr(record, 'client_address'):
            addr = str(record.client_address[0])
            cell_renderer.set_property('text', addr)


    def _cell_data_str(self, column, cell_renderer, tree_model, iter, attrib):
        record = tree_model.get_value(iter, 0)
        if hasattr(record, attrib):
            cell_renderer.set_property('text', getattr(record, attrib))



    def _cursor_changed(self, treeview):
        self.emit('selected-changed')



    def get_selected(self):
        (path, col) = self.treeview.get_cursor()
        return self.liststore[path][0]



# register signal 'changed' with gobject
gobject.type_register(ProxyRecordListWidget)
gobject.signal_new("selected-changed", ProxyRecordListWidget, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())

