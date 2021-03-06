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

from resources import Resources

class ViewManager(gtk.VBox):

    # list of all available views for each object type
    _available_views = {}
    _available_viewmanagers = {}


    def __init__(self, container_notebook, view_object):
        gtk.VBox.__init__(self)

        self._container_notebook = container_notebook
        self._container_notebook_page = self._container_notebook.append_page(self)

        self.view_object = view_object

        self._view_map = {}

        self._toolbar = gtk.Toolbar()
        self._toolbar.set_style(gtk.TOOLBAR_BOTH)
        self._notebook = gtk.Notebook()
        self._notebook.show()

        self.pack_start(self._toolbar, expand=False)
        self.pack_start(self._notebook, expand=True)

        # add views
        if view_object.__class__.__name__ in self._available_views:
            for view_class in self._available_views[view_object.__class__.__name__]:
                view = view_class(view_object)
                self.add_view(view)



    def add_view(self, widget):
        icon = widget.get_icon()
        name = widget.get_name()
        if icon:
            label = gtk.HBox()
            image = gtk.Image()
            image.set_from_pixbuf(self.render_icon(icon, gtk.ICON_SIZE_LARGE_TOOLBAR))
            label.pack_start(image, False, False, 3)
            label.pack_start(gtk.Label(name), False, False, 3)
            label.show_all()
        else:
            label = gtk.Label(name)
        self._view_map[name] = self._notebook.append_page(widget, label)
        widget.show()



    def get_container_notebook(self):
        return self._container_notebook



    def get_menu_icon(self):
        """
        Return the icon to show in the TreeMenu.
        """
        raise Exception(_('Not implemented'))



    def get_menu_name(self):
        """
        Return the text to show in the TreeMenu.
        """
        raise Exception(_('Not implemented'))



    def get_uuid(self):
        """
        Return the uuid of the object the ViewManager manages.
        """
        return self.view_object.uuid



    def selected(self):
        # show toolbar only, if it has some items in it
        if self._toolbar.get_n_items() > 0:
            self._toolbar.show()
        else:
            self._toolbar.hide()

        # show notebook-tabs only if there is more than 1 page
        if self._notebook.get_n_pages() > 1:
            self._notebook.set_show_tabs(True)
            self._notebook.set_show_border(True)
        else:
            self._notebook.set_show_tabs(False)
            self._notebook.set_show_border(False)

        # display our notebook page
        if self._container_notebook_page != None:
            self._container_notebook.set_current_page(self._container_notebook_page)
            self.emit('view-selected')



    def destroy(self):
        self._container_notebook.remove_page(self._container_notebook_page)



    @classmethod
    def register_view(cls, object_type, view):
        if object_type not in cls._available_views:
            cls._available_views[object_type] = []
        cls._available_views[object_type].append(view)



    @classmethod
    def register_viewmanager(cls, object_type, viewmanager):
        """
        :param object_type: this is the name, not the type object
        """
        if object_type in cls._available_viewmanagers:
            raise Exception(_("Already registered a viewmanager for %s") % object_type.__name__)
        cls._available_viewmanagers[object_type] = viewmanager



    @classmethod
    def get_managerclass_for_object(cls, obj):
        if obj.__class__.__name__ in cls._available_viewmanagers:
            return cls._available_viewmanagers[obj.__class__.__name__]
        else:
            return None



    @classmethod
    def build_manager_for_object(cls, container_notebook, obj):
        managerclass = cls._available_viewmanagers[obj.__class__.__name__]
        manager = managerclass(container_notebook, obj)
        return manager




# register signal 'changed' with gobject
gobject.type_register(ViewManager)
gobject.signal_new('view-selected', ViewManager, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())
gobject.signal_new('children-changed', ViewManager, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())


