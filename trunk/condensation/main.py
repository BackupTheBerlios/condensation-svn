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
import xml.etree.cElementTree as ET

import condensation
import condensation.core
import condensation.ui


class Main(condensation.core.CONObject):

    _attribute_definitions = [
        {'name': 'keymanager', 'type': 'KeyManager', 'default': None},
        {'name': 'serverlist', 'type': 'ServerList', 'default': None},
    ]

    _signal_list = (())



    def __init__(self):
        condensation.core.CONObject.__init__(self)



    def delete_event(widget, event, data=None):
        for server in condensation.Server.servers:
            server.disconnect()
        #lib.ProxyServer().stop()
        gtk.main_quit()



    def wakeup(self):
        self.setup()



    def setup(self):
        try:
            # basic stuff
            self._logsink = condensation.LogSink()
            self._navigationhistory = condensation.ui.NavigationHistory()

            # gui stuff
            main_window = condensation.ui.MainWindow()
            main_window.connect("delete-event", self.delete_event)
            main_window.connect("save-action", self.save)

            # create the manager objects
            con_manager = condensation.ui.CondensationViewManager(main_window._notebook, self)
            con_manager.show()
            sl_manager = condensation.ui.ServerListViewManager(main_window._notebook, self.serverlist)
            sl_manager.show()

            # populate treemenu
            treemenu = main_window._treemenu
            treemenu.append(con_manager)
            treemenu.append(sl_manager, con_manager)

            for server in condensation.Server.servers:
                svm = condensation.ui.ServerViewManager(main_window._notebook, server)
                svm.show()
                treemenu.append(svm, sl_manager)
                for vhost in server.vhosts:
                    vhvm = condensation.ui.VHostViewManager(main_window._notebook, vhost)
                    vhvm.show()
                    treemenu.append(vhvm, svm)

            treemenu.expand_all()

            main_window.show()

            logging.info('setup finished!')
        except:
            print "ERROR occured, shutting down..."
            gtk.main_quit()
            raise



    def save(self, source=None):
        logging.info("saving configuration ... ")
        root_elem = ET.Element("configuration")
        root_elem.text = "\n"
        tree = ET.ElementTree(root_elem)
        self.__class__.object_serializer(root_elem, self)
        tree.write("new-condensation.conf.xml", "UTF-8")
        logging.info("saving configuration done")



