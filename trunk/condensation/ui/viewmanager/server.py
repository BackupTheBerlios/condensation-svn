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

        self._server = server

        serverconfig = ServerConfig(self._server)
        serverconfig.show()
        self.add_view('Config', serverconfig)



    def get_menu_text(self):
        return self._server.name



    def get_menu_icon(self):
        return lib.ui.Resources.get_pixbuf('server-disconnected')



