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

import condensation
from resources import Resources
from viewmanager import ViewManager


class CondensationViewManager(ViewManager):


    def __init__(self, containing_notebook, view_object):
        ViewManager.__init__(self, containing_notebook, view_object)

        Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')

        # add views
        for view_class in ViewManager._available_views[condensation.Main]:
            view = view_class(view_object)
            self.add_view(view)


        # populate toolbar
        button = gtk.ToolButton(gtk.STOCK_NEW)
        button.show()
        button.connect('clicked', self._new_server_button_clicked)
        self._toolbar.insert(button, -1)



    def get_menu_text(self):
        return "Condensation"



    def get_menu_icon(self):
        return Resources.get_pixbuf('condensation-icon')



    def _new_server_button_clicked(self, button):
        server = condensation.Server()
        self.view_object.servers.append(server)
        self.emit('children-changed')




# register with ViewManager
ViewManager.register_viewmanager('Main', CondensationViewManager)
