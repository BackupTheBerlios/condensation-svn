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

from vhostconfigview import VHostConfigView


class VHost(lib.ui.ViewManager):

    def __init__(self, containing_notebook, vhost):
        lib.ui.ViewManager.__init__(self, containing_notebook)

        lib.ui.Resources.load_pixbuf('vhost-enabled', 'images/icons/vhost-enabled.svg')
        lib.ui.Resources.load_pixbuf('vhost-disabled', 'images/icons/vhost-disabled.svg')

        lib.ui.Resources.load_pixbuf('configuration-icon', 'images/icons/configuration.svg')

        self._vhost = vhost

        # add views
        vhostconfig = VHostConfigView(self._vhost)
        self.add_view(vhostconfig, 'Config', 'configuration-icon')



    def get_menu_text(self):
        return self._vhost.name



    def get_menu_icon(self):
        return lib.ui.Resources.get_pixbuf('vhost-disabled')



