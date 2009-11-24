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

from viewmanager import ViewManager


class CondensationViewManager(ViewManager):


    def __init__(self, containing_notebook, view_object):
        ViewManager.__init__(self, containing_notebook, view_object)

        condensation.ui.Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')
        condensation.ui.Resources.load_pixbuf('view-log-icon', 'images/icons/view-log.svg')
        condensation.ui.Resources.load_pixbuf('python-console-icon', 'images/icons/python-terminal.svg')

        # add views
        logview = condensation.ui.LogView(self.view_object._logsink)
        self.add_view(logview, 'Application Log', 'view-log-icon')

        #consoleview = PythonConsoleView()
        #self.add_view(consoleview, 'Python Console', 'python-console-icon')



    def get_menu_text(self):
        return "Condensation"



    def get_menu_icon(self):
        return condensation.ui.Resources.get_pixbuf('condensation-icon')

