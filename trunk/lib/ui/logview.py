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
import logging
import pango


class LogView(gtk.VBox):
    """
    Shows the content of a text-file.
    """

    def __init__(self, logsink):
        gtk.VBox.__init__(self)

        scrolled_window =  gtk.ScrolledWindow()
        self.add(scrolled_window)
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        self.textview = gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        self.textview.set_wrap_mode(gtk.WRAP_NONE)
        self.textview.modify_font(pango.FontDescription("Monospace"))
        scrolled_window.add(self.textview)
        scrolled_window.show_all()

        self.buffer = self.textview.get_buffer()
        self.buffer.set_text(logsink.get_text())
        logsink.connect_signal('new-record', self.new_record)




    def new_record(self, logsink, new_index):
        self.buffer.insert_at_cursor("\n"+logsink.get_record_text(new_index))


