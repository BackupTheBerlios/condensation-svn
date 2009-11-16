#!/usr/bin/env python
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

import cProfile
import gobject
import gtk
import logging
import tempfile
import time # only for sleep, remove later

import lib
import lib.ui
import condensation
import condensation.ui


def delete_event(widget, event, data=None):
    lib.ProxyServer().stop()
    gtk.main_quit()



def setup_logging():
    global logsink
    # logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s|%(levelname)-7s|%(name)-18s - %(message)s")

    # Log to a temporary file.
    templog = tempfile.mkstemp('.log', 'condensation-')[1]
    ch = logging.FileHandler(templog)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Log to sys.stderr
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Log to LogSink
    logsink = lib.LogSink()
    logsink.setFormatter(formatter)
    logger.addHandler(logsink)

    logging.info('Logging started ...')



def load_config():
    # load config into memory
    import xml.etree.cElementTree as ET
    et = ET.parse("condensation.conf.xml")


    # load key manager
    keys_elem = et.find("keys")
    if keys_elem != None:
        keymanager = lib.crypto.KeyManager.object_deserializer(keys_elem)
    else:
        keymanager = lib.crypto.KeyManager()
    keymanager.get_ssh_auth_key() # generate key if neccessary


    # load servers
    server_elements = et.findall("server")
    for server_elem in server_elements:
        condensation.Server.object_deserializer(server_elem)

    logging.info('configuration read ...')


    # load proxy
    proxy_elem = et.find("proxy")
    if proxy_elem != None:
        proxy = lib.ProxyServer.object_deserializer(proxy_elem)
    else:
        proxy = lib.ProxyServer()
    proxy.start()



def start_up():
    try:
        global splash_screen
        global logsink

        # basic stuff
        setup_logging()
        load_config()


        # gui stuff
        main_window = condensation.ui.MainWindow()
        main_window.connect("delete_event", delete_event)

        # create the manager objects
        con_manager = condensation.ui.CondensationViewManager(main_window._notebook, logsink)
        con_manager.show()
        sl_manager = condensation.ui.ServerListViewManager(main_window._notebook)
        sl_manager.show()
        pro_manager = condensation.ui.ProxyViewManager(main_window._notebook)
        pro_manager.show()

        # populate treemenu
        treemenu = main_window._treemenu
        treemenu.append(con_manager)
        treemenu.append(pro_manager, con_manager)
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




        # show gui
        main_window.show()
        while gtk.events_pending():
            gtk.main_iteration()


        #time.sleep(2)


        # finished, hide splash
        splash_screen.hide()
        splash_Screen = None
        logging.info('setup finished!')

    except:
        gtk.main_quit()
        raise



def main():
    global splash_screen

    gobject.threads_init()

    splash_screen = lib.ui.SplashScreen('images/splash.svg', 600, 400)
    splash_screen.show()

    gobject.idle_add(start_up)
    gtk.main()


# this is needed so pydoc doesn't run the module while importing it
if __name__ == "__main__":
    cProfile.run('main()', 'profile.out')
