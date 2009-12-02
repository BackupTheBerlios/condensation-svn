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

from viewmanager import ViewManager

class TreeMenu(gtk.TreeView):

    def __init__(self, notebook):
        gtk.TreeView.__init__(self)

        self._notebook = notebook

        # create the TreeView and related stuff
        self.cell_icon = gtk.CellRendererPixbuf()
        self.cell_name = gtk.CellRendererText()
        self.tvcol_icon_name = gtk.TreeViewColumn('Server')
        self.tvcol_icon_name.pack_start(self.cell_icon, False)
        self.tvcol_icon_name.pack_start(self.cell_name, True)
        self.tvcol_icon_name.set_cell_data_func(self.cell_icon, self._object_pixbuf)
        self.tvcol_icon_name.set_cell_data_func(self.cell_name, self._object_str)

        self._treestore = gtk.TreeStore(object)
        self.set_model(self._treestore)
        self.append_column(self.tvcol_icon_name)
        self.connect("cursor_changed", self._cursor_changed)
        self.set_enable_search(False)
        self.set_headers_visible(False)
        self.set_enable_tree_lines(True)
        self.get_selection().set_mode(gtk.SELECTION_SINGLE)

        # id => path mapping for inserting new children
        self._uuid_to_treeiter = {}


    # cell data func for TreeView
    def _object_str(self, treeviewcolumn, cell_renderer, model, iter):
        obj = model.get_value(iter, 0)
        cell_renderer.set_property('text', obj.get_menu_text())


    def _object_pixbuf(self, treeviewcolumn, cell_renderer, model, iter):
        obj = model.get_value(iter, 0)
        cell_renderer.set_property('pixbuf', obj.get_menu_icon())


    # callback for TreeView
    def _cursor_changed(self, treeview):
        (path, col) = self.get_cursor()
        self._treestore[path][0].selected()



    # remove dapage from tree
    def remove(self, viewmanager):
        self._treestore.remove(self._uuid_to_treeiter[viewmanager.get_uuid()])
        del self._uuid_to_treeiter[viewmanager.get_uuid()]



    # get selected
    def get_selected(self):
        (path, col) = self.get_cursor()
        if path:
            return self._treestore[path][0]
        else:
            return None



    def build_menu(self, root_obj):
        self.root_obj = root_obj
        self._treestore.clear()
        self._build_menu(self.root_obj)



    def _build_menu(self, obj, parent=None):
        if obj.__class__.__name__ in ViewManager._available_viewmanagers:
            manager = self._create_manager_for_object(obj)
            # add manager to tree
            if parent != None:
                piter = self._uuid_to_treeiter[parent.get_uuid()]
                self._uuid_to_treeiter[manager.get_uuid()] = self._treestore.append(piter, (manager,))
            else:
                self._uuid_to_treeiter[manager.get_uuid()] = self._treestore.append(None, (manager,))
            # if no object is selected (yet) select this
            (path, col) = self.get_cursor()
            if path == None:
                self.set_cursor((0,))
            # add children
            for attr in obj.get_attribute_list():
                attr_def = obj.get_attribute_definition(attr)
                if attr_def.has_key('navigatable') and attr_def['navigatable']:
                    if obj.is_attribute_collection(attr):
                        for elem in obj.__getattr__(attr):
                            self._build_menu(elem, manager)
                    else:
                        self._build_menu(obj.__getattr__(attr), manager)
            return manager
        else:
            return None


    def _create_manager_for_object(self, obj):
        manager = ViewManager.build_manager_for_object(self._notebook, obj)
        manager.connect('children-changed', self._manager_children_changed)
        manager.show()
        return manager



    def _manager_children_changed(self, manager):
        print 'children changed'
        child_uuids = [] # list of uuids as objects found
        object_uuids = {} # map uuid -> object
        menu_uuids = [] # uuids of managers already in menu
        manager_uuids = {} # map uuid -> manager

        # scan object for navigatable attributes
        obj = manager.view_object
        for attr_name in obj.get_attribute_list():
            attr_def = obj.get_attribute_definition(attr_name)
            if attr_def.has_key('navigatable') and attr_def['navigatable']:
                attr_value = obj.__getattr__(attr_name)
                if obj.is_attribute_collection(attr_name):
                    for elem in attr_value:
                        # add, if a viewmanager for the object exists
                        if ViewManager.get_managerclass_for_object(elem):
                            child_uuids.append(elem.uuid)
                            object_uuids[elem.uuid] = elem
                else:
                    # add, if a viewmanager for the object exists
                    if ViewManager.get_managerclass_for_object(attr_value):
                        child_uuids.append(attr_value.uuid)
                        object_uuids[attr_value.uuid] = attr_value

        # collect uuid of children in treemenu
        it = self._uuid_to_treeiter[manager.get_uuid()]
        it = self._treestore.iter_children(it)
        while it:
            m = self._treestore.get_value(it, 0)
            manager_uuids[m.get_uuid()] = m
            menu_uuids.append(m.get_uuid())
            it = self._treestore.iter_next(it)

        # remove items that got deleted
        for uuid in set(menu_uuids) - set(child_uuids):
            print "removed "+str(uuid)
            raise Exception('not implemented yet')
        # add items that were inserted
        for uuid in set(child_uuids) - set(menu_uuids):
            print "added "+str(uuid)
            self._build_menu(object_uuids[uuid], manager)
            menu_uuids.append(uuid)

        # TODO: sort
        # see: http://library.gnome.org/devel/pygtk/stable/class-gtktreestore.html#method-gtktreestore--reorder
