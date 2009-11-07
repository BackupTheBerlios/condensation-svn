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

from serverconfigview import ServerConfigView
from sshterminalview import SSHTerminalView

class Server(lib.ui.ViewManager):

    def __init__(self, containing_notebook, server):
        lib.ui.ViewManager.__init__(self, containing_notebook)

        lib.ui.Resources.load_pixbuf('server-connected', 'images/icons/server-connected.svg')
        lib.ui.Resources.load_pixbuf('server-disconnected', 'images/icons/server-disconnected.svg')

        lib.ui.Resources.load_pixbuf('configuration-icon', 'images/icons/configuration.svg')
        lib.ui.Resources.load_pixbuf('ssh-terminal-icon', 'images/icons/ssh-terminal.svg')

        self._server = server

        # add views
        serverconfig = ServerConfigView(self._server)
        self.add_view(serverconfig, 'Config', 'configuration-icon')

        sshterminal = SSHTerminalView(self._server)
        self.add_view(sshterminal, 'SSH Terminal', 'ssh-terminal-icon')


        # populate toolbar
        self.connect_button = gtk.ToolButton(gtk.STOCK_CONNECT)
        self._toolbar.insert(self.connect_button, -1)
        self.connect_button.show()

        self.disconnect_button = gtk.ToolButton(gtk.STOCK_DISCONNECT)
        self._toolbar.insert(self.disconnect_button, -1)
        self.disconnect_button.show()

        self.update()



    def update(self):
        self.connect_button.set_property('sensitive', not self._server.get_connected())
        self.disconnect_button.set_property('sensitive', self._server.get_connected())


    def get_menu_text(self):
        return self._server.name



    def get_menu_icon(self):
        if self._server.get_connected():
            return lib.ui.Resources.get_pixbuf('server-connected')
        else:
            return lib.ui.Resources.get_pixbuf('server-disconnected')



