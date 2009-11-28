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

import gobject
import gtk
import logging

import condensation
import condensation.core
import condensation.ui


class Main(condensation.core.CONObject):

    _attribute_definitions = [
        {'name': 'keymanager', 'type': 'KeyManager', 'default': None, 'navigatable': True},
        {'name': 'servers', 'type': 'Server[]', 'default': [], 'navigatable': True},
    ]

    _signal_list = (())



    def __init__(self):
        condensation.core.CONObject.__init__(self)



    def delete_event(widget, event, data=None):
        for server in condensation.Server.servers:
            server.disconnect()
        condensation.PluginManager().cleanup_plugins()
        gtk.main_quit()



    def wakeup(self):
        self.setup()



    def setup(self):
        try:
            # basic stuff
            self._logsink = condensation.LogSink()
            self._navigationhistory = condensation.ui.NavigationHistory()

            # gui stuff
            self._main_window = condensation.ui.MainWindow()
            self._main_window.connect("delete-event", self.delete_event)
            self._main_window.connect("save-action", self.save)

            # populate treemenu
            treemenu = self._main_window._treemenu
            treemenu.build_menu(self)
            treemenu.expand_all()

            self._main_window.show()

            logging.info('setup finished!')
        except:
            print "ERROR occured, shutting down..."
            gtk.main_quit()
            raise



    def save(self, source=None):
        import xml.etree.cElementTree as ET
        logging.info("saving configuration ... ")
        root_elem = ET.Element("configuration")
        root_elem.text = "\n"
        tree = ET.ElementTree(root_elem)
        self.__class__.object_serializer(root_elem, self)
        tree.write("new-condensation.conf.xml", "UTF-8")
        logging.info("saving configuration done")



