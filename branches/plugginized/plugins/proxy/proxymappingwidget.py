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


class ProxyMappingWidget(gtk.Frame):
    """
    Widget used for editing a list of integers
    """

    def __init__(self, initial_map):
        gtk.Frame.__init__(self)
        hbox = gtk.HBox()

        self.liststore = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_BOOLEAN, gobject.TYPE_STRING)
        self.treemodelsort = gtk.TreeModelSort(self.liststore)
        self.treemodelsort.set_sort_column_id(0, gtk.SORT_ASCENDING)
        self.treeview = gtk.TreeView(self.treemodelsort)

        # domain column
        self._domain_values = gtk.ListStore(gobject.TYPE_STRING)
        self._domain_values.append(('Test',))

        self.column_domain = gtk.TreeViewColumn('Domain')
        self.treeview.append_column(self.column_domain)
        self.cell_domain = gtk.CellRendererCombo()
        self.cell_domain.set_property('editable', True)
        self.cell_domain.set_property('model', self._domain_values)
        self.cell_domain.set_property('text-column', 0)
        self.cell_domain.connect('edited', self._domain_edited_callback)
        self.column_domain.pack_start(self.cell_domain, True)
        self.column_domain.add_attribute(self.cell_domain, 'text', 0)
        self.column_domain.set_property('resizable', True)
        self.column_domain.set_sort_column_id(0)

        # use ssh column
        self.column_ssh = gtk.TreeViewColumn('Use SSH')
        self.treeview.append_column(self.column_ssh)
        self.cell_ssh = gtk.CellRendererToggle()
        self.cell_ssh.set_property('activatable', True)
        self.cell_ssh.connect('toggled', self._ssh_toggled_callback)
        self.column_ssh.pack_start(self.cell_ssh, True)
        self.column_ssh.add_attribute(self.cell_ssh, 'active', 1)
        self.column_ssh.set_property('resizable', True)
        self.column_ssh.set_sort_column_id(1)

        # target column
        self._target_values = gtk.ListStore(gobject.TYPE_STRING)
        self._target_values.append(('Test',))

        self.column_target = gtk.TreeViewColumn('Connect To')
        self.treeview.append_column(self.column_target)
        self.cell_target = gtk.CellRendererCombo()
        self.cell_target.set_property('editable', True)
        self.cell_target.set_property('model', self._target_values)
        self.cell_target.set_property('text-column', 0)
        self.cell_target.connect('edited', self._target_edited_callback)
        self.column_target.pack_start(self.cell_target, True)
        self.column_target.add_attribute(self.cell_target, 'text', 2)
        self.column_target.set_property('resizable', True)
        self.column_target.set_sort_column_id(2)

        # general treeview stuff
        self.treeview.set_search_column(0)
        self.treeview.set_reorderable(True)
        self.treeview.set_headers_visible(True)
        self.treeview.set_rules_hint(True)
        self.treeview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)

        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.add(self.treeview)
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolled_window.set_property('shadow-type', gtk.SHADOW_IN)

        vbuttonbox = gtk.VButtonBox()
        vbuttonbox.set_layout(gtk.BUTTONBOX_START)
        button = gtk.Button(stock=gtk.STOCK_ADD)
        button.connect("clicked", self.add_button_callback)
        vbuttonbox.add(button)
        button = gtk.Button(stock=gtk.STOCK_DELETE)
        button.connect("clicked", self.delete_button_callback)
        vbuttonbox.add(button)

        hbox.pack_start(scrolled_window, expand=True, fill=True, padding=0)
        hbox.pack_end(vbuttonbox, expand=False, fill=False, padding=10)

        self.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        self.add(hbox)
        self.show_all()

        for domain in initial_map.keys():
            self.liststore.append([domain, initial_map[domain][0], initial_map[domain][1]])







    def get_map(self):
        #values = []
        #iter = self.liststore.get_iter_first()
        #while iter != None:
            #values.append(self.liststore.get_value(iter, 0))
            #iter = self.liststore.iter_next(iter)
        #return values
        pass


    def set_map(self, new_list):
        #self.liststore.clear()
        #for item in new_list:
            #self.liststore.append([item])
        #self.emit('changed')
        pass


    def _domain_edited_callback(self, cellrenderertext, sorted_path, new_text):
        path = self.treemodelsort.convert_path_to_child_path(sorted_path)
        self.liststore[path][0] = new_text
        self.emit('changed')


    def _ssh_toggled_callback(self, cellrenderertoggle, sorted_path):
        # TODO: if target is not specified or has no SSH connection, don't allow true....
        path = self.treemodelsort.convert_path_to_child_path(sorted_path)
        self.liststore[path][1] = not self.liststore[path][1]
        self.emit('changed')


    def _target_edited_callback(self, cellrenderertext, sorted_path, new_text):
        path = self.treemodelsort.convert_path_to_child_path(sorted_path)
        self.liststore[path][2] = new_text
        self.emit('changed')


    def add_button_callback(self, button):
        self.liststore.append(('', False, ''))
        self.emit('changed')


    def delete_button_callback(self, button):
        (model, pathlist) = self.treeview.get_selection().get_selected_rows()
        iterlist = []
        for sorted_path in pathlist:
            unsorted_path = self.treemodelsort.convert_path_to_child_path(sorted_path)
            iter = self.liststore.get_iter(unsorted_path)
            iterlist.append(iter)
        if iterlist:
            for iter in iterlist:
                self.liststore.remove(iter)
            self.emit('changed')


# register signal 'changed' with gobject
gobject.type_register(ProxyMappingWidget)
gobject.signal_new("changed", ProxyMappingWidget, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())
