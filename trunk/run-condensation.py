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

import gtk


class SplashScreen(gtk.Window):

    def __init__(self, image_path, size_x, size_y):
        gtk.Window.__init__(self, type=gtk.WINDOW_TOPLEVEL)
        self.set_size_request(size_x, size_y)
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_keep_above(True)
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_SPLASHSCREEN)

        pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(image_path, size_x, size_y)
        image = gtk.Image()
        image.set_from_pixbuf(pixbuf)
        self.add(image)
        image.show()



def setup_logging():
    import logging
    import tempfile
    import condensation

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
    ch.setLevel(logging.WARNING)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Log to LogSink
    logsink = condensation.LogSink()
    logsink.setFormatter(formatter)
    logger.addHandler(logsink)

    logging.info(_('Logging started ...'))





def start_up():
    global splash_screen

    import time
    time.sleep(0.5) # give the splash-screen time to show

    # setup gettext
    import gettext
    #import __builtin__
    #__builtin__._ = gettext.gettext
    #gettext.bindtextdomain('Condensation', 'i18n')
    #gettext.textdomain('Condensation')
    gettext.install('Condensation', 'i18n', unicode=1)

    # logging
    setup_logging()

    # load plugins
    import condensation
    pluginmanager = condensation.PluginManager()
    pluginmanager.load_plugins()

    # load configuration
    try:
        # try to load configuraion
        import xml.etree.cElementTree as ET
        et = ET.parse("condensation.conf.xml")
        main = condensation.Main.object_deserializer(et.getroot())
    except IOError, e:
        # probably file not found
        logging.warn(_("Could not load configuration file"))
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



def main():
    global splash_screen

    import gobject
    import gtk
    gobject.threads_init()

    splash_screen = SplashScreen('images/splash.svg', 600, 400)
    splash_screen.show()

    gobject.idle_add(start_up)
    gtk.main()


# this is needed so pydoc doesn't run the module while importing it
if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', 'profile.out')
