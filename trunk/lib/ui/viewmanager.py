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

from resources import Resources

class ViewManager(gtk.VBox):

    def __init__(self, container_notebook):
        gtk.VBox.__init__(self)
        self._container_notebook = container_notebook
        self._container_notebook_page = self._container_notebook.append_page(self)
        self._view_map = {}

        self._toolbar = gtk.Toolbar()
        self._toolbar.show()
        self._notebook = gtk.Notebook()
        self._notebook.show()

        self.pack_start(self._toolbar, expand=False)
        self.pack_start(self._notebook, expand=True)



    def add_view(self, widget, name, image_id = None):
        if image_id:
            label = gtk.HBox()
            image = gtk.Image()
            image.set_from_pixbuf(Resources.get_pixbuf(image_id))
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
        Return the item to be shown in the TreeView.
        """
        raise Exception("Not Implemented!")



    def get_menu_name(self):
        raise Exception("Not Implemented!")



    def selected(self):
        if self._container_notebook_page != None:
            self._container_notebook.set_current_page(self._container_notebook_page)



    def destroy(self):
        self._container_notebook.remove_page(self._container_notebook_page)




