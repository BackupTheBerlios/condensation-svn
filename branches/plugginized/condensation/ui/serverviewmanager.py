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
from serverconfigview import ServerConfigView
from viewmanager import ViewManager

class ServerViewManager(ViewManager):

    def __init__(self, containing_notebook, view_object):
        ViewManager.__init__(self, containing_notebook, view_object)

        Resources.load_pixbuf('server-connected', 'images/icons/server-connected.svg')
        Resources.load_pixbuf('server-disconnected', 'images/icons/server-disconnected.svg')

        Resources.load_pixbuf('configuration-icon', 'images/icons/configuration.svg')
        Resources.load_pixbuf('ssh-terminal-icon', 'images/icons/ssh-terminal.svg')

        self.view_object.connect_signal('changed', self.on_server_changed)

        # add views
        serverconfig = ServerConfigView(self.view_object)
        self.add_view(serverconfig, 'Config', 'configuration-icon')

        #sshterminal = SSHTerminalView(self.view_object)
        #self.add_view(sshterminal, 'SSH Terminal', 'ssh-terminal-icon')


        # populate toolbar
        self.connect_button = gtk.ToolButton(gtk.STOCK_CONNECT)
        self.connect_button.connect('clicked', self.action_connect)
        self._toolbar.insert(self.connect_button, -1)
        self.connect_button.show()

        self.disconnect_button = gtk.ToolButton(gtk.STOCK_DISCONNECT)
        self.disconnect_button.connect('clicked', self.action_disconnect)
        self._toolbar.insert(self.disconnect_button, -1)
        self.disconnect_button.show()

        self.update()



    def action_connect(self, action=None):
         self.view_object.connect_to_server()



    def action_disconnect(self, action=None):
        self.view_object.disconnect()



    def on_server_changed(self, server):
        self.update()



    def update(self):
        self.connect_button.set_property('sensitive', not self.view_object.get_connected())
        self.disconnect_button.set_property('sensitive', self.view_object.get_connected())


    def get_menu_text(self):
        return self.view_object.name



    def get_menu_icon(self):
        if self.view_object.get_connected():
            return Resources.get_pixbuf('server-connected')
        else:
            return Resources.get_pixbuf('server-disconnected')



