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
import condensation.ui.viewmanager


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



def start_up():
    try:
        global splash_screen
        global logsink
        # basic stuff
        setup_logging()


        # gui stuff
        main_window = condensation.ui.MainWindow()

        # create the manager objects
        con_manager = condensation.ui.viewmanager.Condensation(main_window._notebook, logsink)
        con_manager.show()
        sl_manager = condensation.ui.viewmanager.ServerList(main_window._notebook)
        sl_manager.show()

        # populate treemenu
        treemenu = main_window._treemenu
        treemenu.append(con_manager)
        treemenu.append(sl_manager, con_manager)



        #time.sleep(2)


        # show gui
        main_window.show()
        while gtk.events_pending():
            gtk.main_iteration()


        time.sleep(2)


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
