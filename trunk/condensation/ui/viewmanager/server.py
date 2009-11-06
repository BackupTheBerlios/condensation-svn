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

import lib.ui

from serverconfig import ServerConfig

class Server(lib.ui.ViewManager):

    def __init__(self, containing_notebook, server):
        lib.ui.ViewManager.__init__(self, containing_notebook)

        lib.ui.Resources.load_pixbuf('server-connected', 'images/icons/server-connected.svg')
        lib.ui.Resources.load_pixbuf('server-disconnected', 'images/icons/server-disconnected.svg')

        lib.ui.Resources.load_pixbuf('configuration-icon', 'images/icons/configuration.svg')

        self._server = server

        # add views
        serverconfig = ServerConfig(self._server)
        self.add_view(serverconfig, 'Config', 'configuration-icon')

        # populate toolbar
        connect_button = gtk.ToggleToolButton(gtk.STOCK_CONNECT)
        self._toolbar.insert(connect_button, -1)
        connect_button.show()

        disconnect_button = gtk.ToolButton(gtk.STOCK_DISCONNECT)
        self._toolbar.insert(disconnect_button, -1)
        disconnect_button.show()

        #self.show_all()



    def get_menu_text(self):
        return self._server.name



    def get_menu_icon(self):
        if self._server.get_connected():
            return lib.ui.Resources.get_pixbuf('server-connected')
        else:
            return lib.ui.Resources.get_pixbuf('server-disconnected')



