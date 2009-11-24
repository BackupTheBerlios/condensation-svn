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
import gtkmozembed
import logging


class MozEmbedView(gtk.VBox):


    def __init__(self, vhost):
        gtk.VBox.__init__(self)
        self.vhost = vhost

        # logging
        self.logger = logging.getLogger('MozEmbed')

        # controls
        self.combobox = gtk.combo_box_entry_new_text()
        #for domain in vhost.domains:
        #    self.combobox.append_text('http://'+domain)
        self.pack_start(self.combobox, expand=False, fill=True, padding=0)

        self.combobox.child.connect('activate', self.on_combobox_activate)


        # mozembed
        self.mozembed = gtkmozembed.MozEmbed()
        self.pack_start(self.mozembed, expand=True, fill=True, padding=0)
        self.mozembed.connect('open_uri', self.on_open_uri)

        self.show_all()



    def on_combobox_activate(self, entry):
        self.mozembed.load_url(self.combobox.child.get_text())



    def on_open_uri(self, mozembed, uri, *data):
        self.logger.info('open_uri: '+uri)
        return False

