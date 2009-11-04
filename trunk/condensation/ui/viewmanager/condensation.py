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


class Condensation(lib.ui.ViewManager):


    def __init__(self, containing_notebook, logsink):
        lib.ui.ViewManager.__init__(self, containing_notebook)

        lib.ui.Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')

        logview = lib.ui.LogView(logsink)
        logview.show()
        self.add_view('Application Log', logview)

        consoleview = lib.ui.PythonConsoleView()
        consoleview.show()
        self.add_view('Python Console', consoleview)



    def get_menu_text(self):
        return "Condensation"



    def get_menu_icon(self):
        return lib.ui.Resources.get_pixbuf('condensation-icon')


