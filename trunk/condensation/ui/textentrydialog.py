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

class TextEntryDialog(gtk.MessageDialog):

    def __init__(self, title, text, label, info='', input_hidden=False):
        gtk.MessageDialog.__init__(
            self,
            parent=None,
            flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
            type=gtk.MESSAGE_QUESTION,
            buttons=gtk.BUTTONS_OK_CANCEL,
            message_format=None)
        self.set_title(title)
        self.set_markup(text)
        self.format_secondary_markup(info)
        self.entry = gtk.Entry()
        self.entry.set_visibility(not input_hidden)
        self.entry.connect("activate", self._entry_activated, gtk.RESPONSE_OK)

        hbox = gtk.HBox()
        hbox.pack_start(gtk.Label(label), False, 5, 5)
        hbox.pack_end(self.entry)

        self.vbox.pack_end(hbox, True, True, 0)
        self.vbox.show_all()



    def _entry_activated(self, entry, response):
        self.response(response)



    def get_entry_text(self):
        return self.entry.get_text()



    @classmethod
    def run_dialog(cls, title, text, label, info, input_hidden):
        dia = cls(title, text, label, info, input_hidden)
        dia.run()
        text_input = dia.get_entry_text()
        dia.hide()
        dia.destroy()
        return text_input
