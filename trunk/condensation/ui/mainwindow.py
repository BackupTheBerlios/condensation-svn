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
import gtk.gdk
import logging

import condensation
from resources import Resources
from treemenu import TreeMenu


class MainWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_title("Condensation")
        self.set_default_size(800, 600)

        Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')
        self.set_icon(Resources.get_pixbuf('condensation-icon'))

        # toolbar
        self._toolbar = gtk.Toolbar()
        self._toolbar.set_property('toolbar-style', gtk.TOOLBAR_BOTH)

        button = gtk.ToolButton(gtk.STOCK_GO_BACK)
        #button.connect('clicked', self._save_button_clicked)
        self._toolbar.insert(button, -1)

        self._forward_button = gtk.MenuToolButton(gtk.STOCK_GO_FORWARD)
        #button.connect('clicked', self._save_button_clicked)
        self._toolbar.insert(self._forward_button, -1)

        self._toolbar.insert(gtk.SeparatorToolItem(), -1)

        button = gtk.ToolButton(gtk.STOCK_SAVE)
        button.connect('clicked', self._save_button_clicked)
        self._toolbar.insert(button, -1)

        separator = gtk.SeparatorToolItem()
        separator.set_expand(True)
        separator.set_draw(False)
        self._toolbar.insert(separator, -1)

        button = gtk.ToolButton(gtk.STOCK_QUIT)
        button.connect('clicked', self._quit_button_clicked)
        self._toolbar.insert(button, -1)


        # treemenu
        self._treemenu = TreeMenu()
        sw_treemenu = gtk.ScrolledWindow()
        sw_treemenu.add(self._treemenu)
        sw_treemenu.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw_treemenu.set_size_request(200, 200)

        # notebook
        self._notebook = gtk.Notebook()
        self._notebook.set_property('show-border', False)
        self._notebook.set_property('scrollable', True)
        self._notebook.set_show_tabs(False)

        paned = gtk.HPaned()
        paned.add1(sw_treemenu)
        paned.add2(self._notebook)

        vbox = gtk.VBox()
        vbox.pack_start(self._toolbar, expand=False, fill=True)
        vbox.pack_start(paned, expand=True, fill=True)
        self.add(vbox)
        vbox.show_all()



    def _save_button_clicked(self, button):
        self.emit("save-action")



    def _quit_button_clicked(self, button):
        self.emit('delete-event', gtk.gdk.Event(gtk.gdk.DELETE))



# register signal 'changed' with gobject
gobject.type_register(MainWindow)
gobject.signal_new("save-action", MainWindow, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())




