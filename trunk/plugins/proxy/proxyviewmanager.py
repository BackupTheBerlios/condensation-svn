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
import condensation.ui

from proxyconfigview import ProxyConfigView
from proxyinterceptview import ProxyInterceptView
from proxyredirectionsview import ProxyRedirectionsView
from proxyserver import ProxyServer


class ProxyViewManager(condensation.ui.ViewManager):


    def __init__(self, containing_notebook, view_object):
        condensation.ui.ViewManager.__init__(self, containing_notebook, view_object)


    def get_menu_text(self):
        return "Proxy"


    def get_menu_icon(self):
        return condensation.ui.Resources.get_pixbuf('proxy-icon')

