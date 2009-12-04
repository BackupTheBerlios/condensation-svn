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


__plugin_name__ = 'Python Console'
__doc__ = """provides a Python console"""

import os.path

def __install_plugin__():
    import condensation
    import condensation.ui
    from pythonconsoleview import PythonConsoleView
    condensation.ui.ViewManager.register_view('Main', PythonConsoleView)
    condensation.ui.Resources.load_pixbuf('python-console-icon', os.path.join(__path__[0], 'python-console.svg'))

