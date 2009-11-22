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

import gobject
import gtk
import cProfile
import time
import xml.etree.cElementTree as ET

import lib.ui

import condensation


def start_up():
    global splash_screen

    et = ET.parse("condensation.conf.xml")
    condensation.Main.object_deserializer(et.getroot())

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

    splash_screen = lib.ui.SplashScreen('images/splash.svg', 600, 400)
    splash_screen.show()

    gobject.idle_add(start_up)
    gtk.main()


# this is needed so pydoc doesn't run the module while importing it
if __name__ == "__main__":
    cProfile.run('main()', 'profile.out')
