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

from lib.ui import TreeMenu

class MainWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_title("Condensation")
        self.set_default_size(800, 600)

        self._treemenu = TreeMenu()

        # scrolled window for treeview
        sw_treemenu = gtk.ScrolledWindow()
        sw_treemenu.add_with_viewport(self._treemenu)
        sw_treemenu.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw_treemenu.set_size_request(200, 200)

        self._notebook = gtk.Notebook()
        self._notebook.set_property('show-border', False)
        self._notebook.set_property('scrollable', True)
        self._notebook.set_show_tabs(False)
        paned = gtk.HPaned()
        paned.add1(sw_treemenu)
        paned.add2(self._notebook)
        self.add(paned)
        paned.show_all()



