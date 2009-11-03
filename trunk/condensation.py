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

import lib.ui
import condensation


def setup_logging():
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

    # Log to DALogView
    #self.logview = DALogView()
    #self.logview.setFormatter(formatter)
    #logger.addHandler(self.logview)



def start_up():
    try:
        global splash_screen
        # basic stuff
        setup_logging()


        # gui stuff
        main_window = condensation.MainWindow()

        treemenu = main_window._treemenu
        treemenu.append(condensation.CondensationManager(main_window._notebook))



        #time.sleep(2)


        # show gui
        main_window.show()
        while gtk.events_pending():
            gtk.main_iteration()


        #time.sleep(2)


        # finished, hide splash
        splash_screen.hide()
        splash_Screen = None

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
