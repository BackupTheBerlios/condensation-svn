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

        self.treestore = gtk.TreeStore(object)
        self.set_model(self.treestore)
        self.append_column(self.tvcol_icon_name)
        self.connect("cursor_changed", self._cursor_changed)
        self.set_enable_search(False)
        self.set_headers_visible(False)
        self.set_enable_tree_lines(True)
        self.get_selection().set_mode(gtk.SELECTION_SINGLE)

        # id => path mapping for inserting new children
        self._id_to_treeiter = {}


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
        self.treestore[path][0].selected()



    # remove dapage from tree
    def remove(self, viewmanager):
        self.treestore.remove(self._id_to_treeiter[viewmanager.get_uuid()])
        del self._id_to_treeiter[viewmanager.get_uuid()]



    # get selected
    def get_selected(self):
        (path, col) = self.get_cursor()
        if path:
            return self.treestore[path][0]
        else:
            return None



    def build_menu(self, obj, parent=None):
        if obj.__class__.__name__ in ViewManager._available_viewmanagers:
            # create ViewManager
            managerclass = ViewManager._available_viewmanagers[obj.__class__.__name__]
            manager = managerclass(self._notebook, obj)
            manager.show()
            # add manager to tree
            if parent != None:
                piter = self._id_to_treeiter[parent.get_uuid()] # TODO: raise something if not found
                self._id_to_treeiter[manager.get_uuid()] = self.treestore.append(piter, (manager,))
            else:
                self._id_to_treeiter[manager.get_uuid()] = self.treestore.append(None, (manager,))
            (path, col) = self.get_cursor()
            # if this is the first item in the tree, select it
            if path == None:
                self.set_cursor((0,))
            # add children
            for attr in obj.get_attribute_list():
                attr_def = obj.get_attribute_definition(attr)
                if attr_def.has_key('navigatable') and attr_def['navigatable']:
                    if obj.is_attribute_collection(attr):
                        for elem in obj.__getattr__(attr):
                            self.build_menu(elem, manager)
                    else:
                        self.build_menu(obj.__getattr__(attr), manager)
