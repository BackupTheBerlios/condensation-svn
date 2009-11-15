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


class IntegerListWidget(gtk.HBox):
    """
    Widget used for editing a list of integers
    """

    def __init__(self, min, max, integerlist=[]):
        gtk.HBox.__init__(self)

        self.liststore = gtk.ListStore(int)
        self.treeview = gtk.TreeView(self.liststore)
        self.tvcolumn = gtk.TreeViewColumn('Column 0')
        self.treeview.append_column(self.tvcolumn)
        self.cell = gtk.CellRendererSpin()
        self.cell.set_property('adjustment', gtk.Adjustment(lower=min, upper=max, step_incr=1))
        self.cell.set_property('editable', True)
        self.cell.connect('edited', self.edited_callback)
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.add_attribute(self.cell, 'text', 0)
        self.tvcolumn.set_sort_column_id(0)
        self.treeview.set_search_column(0)
        self.treeview.set_reorderable(True)
        self.treeview.set_headers_visible(False)
        self.treeview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)

        for item in integerlist:
            self.liststore.append([item])

        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.add(self.treeview)
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

        vbuttonbox = gtk.VButtonBox()
        vbuttonbox.set_layout(gtk.BUTTONBOX_START)
        button = gtk.Button(stock=gtk.STOCK_ADD)
        button.connect("clicked", self.add_button_callback)
        vbuttonbox.add(button)
        button = gtk.Button(stock=gtk.STOCK_DELETE)
        button.connect("clicked", self.delete_button_callback)
        vbuttonbox.add(button)

        self.pack_start(scrolled_window, expand=True, fill=True, padding=0)
        self.pack_end(vbuttonbox, expand=False, fill=False, padding=10)

        self.show_all()



    def get_list(self):
        values = []
        iter = self.liststore.get_iter_first()
        while iter != None:
            values.append(self.liststore.get_value(iter, 0))
            iter = self.liststore.iter_next(iter)
        return values



    def set_list(self, new_list):
        self.liststore.clear()
        for item in new_list:
            self.liststore.append([item])
        self.emit('changed')



    def edited_callback(self, cellrendererspin, path, new_text):
        try:
            self.liststore[path][0] = int(new_text)
            self.emit('changed')
        except ValueError, e:
            pass



    def add_button_callback(self, button):
        self.liststore.append([0])
        self.emit('changed')



    def delete_button_callback(self, button):
        (model, pathlist) = self.treeview.get_selection().get_selected_rows()
        iterlist = []
        for path in pathlist:
            iterlist.append(self.liststore.get_iter(path))
        if iterlist:
            for iter in iterlist:
                self.liststore.remove(iter)
            self.emit('changed')



# register signal 'changed' with gobject
gobject.type_register(IntegerListWidget)
gobject.signal_new("changed", IntegerListWidget, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())
