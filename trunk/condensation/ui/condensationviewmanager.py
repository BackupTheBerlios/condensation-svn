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
import xml.etree.cElementTree as ET

import lib.crypto
import lib.ui

import condensation
from pythonconsoleview import PythonConsoleView


class CondensationViewManager(lib.ui.ViewManager):


    def __init__(self, containing_notebook, logsink):
        lib.ui.ViewManager.__init__(self, containing_notebook)

        lib.ui.Resources.load_pixbuf('condensation-icon', 'images/icons/condensation.svg')
        lib.ui.Resources.load_pixbuf('view-log-icon', 'images/icons/view-log.svg')
        lib.ui.Resources.load_pixbuf('python-console-icon', 'images/icons/python-terminal.svg')

        # add views
        logview = lib.ui.LogView(logsink)
        self.add_view(logview, 'Application Log', 'view-log-icon')

        consoleview = PythonConsoleView()
        self.add_view(consoleview, 'Python Console', 'python-console-icon')

        # populate toolbar
        save_button = gtk.ToolButton(gtk.STOCK_SAVE)
        save_button.connect('clicked', self._save_button_clicked)
        self._toolbar.insert(save_button, -1)
        save_button.show()




    def get_menu_text(self):
        return "Condensation"



    def get_menu_icon(self):
        return lib.ui.Resources.get_pixbuf('condensation-icon')



    def _save_button_clicked(self, button):
        doc_elem = ET.Element("configuration")
        doc_elem.text = "\n"
        tree = ET.ElementTree(doc_elem)

        # save keymanager
        key_elem = ET.SubElement(doc_elem, "keys")
        key_elem.tail = "\n"
        lib.crypto.KeyManager.object_serializer(key_elem, lib.crypto.KeyManager())

        # save servers
        for server in condensation.Server.servers:
            server_elem = ET.SubElement(doc_elem, "server")
            server_elem.tail = "\n"
            condensation.Server.object_serializer(server_elem, server)

        # save proxy
        key_elem = ET.SubElement(doc_elem, "proxy")
        key_elem.tail = "\n"
        lib.ProxyServer.object_serializer(key_elem, lib.ProxyServer())

        # write file
        tree.write("new-condensation.conf.xml", "UTF-8")
