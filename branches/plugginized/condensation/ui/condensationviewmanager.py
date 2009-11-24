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

import condensation.ui
from viewmanager import ViewManager


class CondensationViewManager(ViewManager):


    def __init__(self, containing_notebook, view_object):
        ViewManager.__init__(self, containing_notebook, view_object)

        condensation.ui.Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')

        # add views
        for view_class in ViewManager._available_views[condensation.Main]:
            view = view_class(view_object)
            self.add_view(view)



    def get_menu_text(self):
        return "Condensation"



    def get_menu_icon(self):
        return condensation.ui.Resources.get_pixbuf('condensation-icon')

