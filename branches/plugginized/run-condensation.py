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
import time
import xml.etree.cElementTree as ET

import condensation
import condensation.ui


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
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Log to LogSink
    logsink = condensation.LogSink()
    logsink.setFormatter(formatter)
    logger.addHandler(logsink)

    logging.info('Logging started ...')





def start_up():
    global splash_screen

    setup_logging()

    # load plugins
    pluginmanager = condensation.PluginManager()
    pluginmanager.load_plugins()

    try:
        # try to load configuraion
        et = ET.parse("condensation.conf.xml")
        condensation.Main.object_deserializer(et.getroot())
    except IOError, e:
        # probably file not found
        logging.warn("Could not load configuration file")
        main = condensation.Main()
        main.setup()
    except:
        # oh, oh....
        gtk.main_quit()
        raise

    while gtk.events_pending():
        gtk.main_iteration()
    time.sleep(0.5)
    while gtk.events_pending():
        gtk.main_iteration()
    time.sleep(1)

    # finished, hide splash
    splash_screen.hide()
    splash_screen = None

    #con = condensation.Main()
    #con.setup()


def main():
    global splash_screen
    gobject.threads_init()

    splash_screen = condensation.ui.SplashScreen('images/splash.svg', 600, 400)
    splash_screen.show()

    gobject.idle_add(start_up)
    gtk.main()


# this is needed so pydoc doesn't run the module while importing it
if __name__ == "__main__":
    cProfile.run('main()', 'profile.out')
