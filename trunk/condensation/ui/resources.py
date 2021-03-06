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

class Resources(object):

    _iconfactory = None

    @classmethod
    def image_label_button(cls, image_id, label_text):
        box = gtk.HBox(False, 0)
        box.set_border_width(0)

        # Now on to the image stuff
        image = gtk.Image()
        image.set_from_pixbuf(cls.get_pixbuf(image_id))

        # Create a label for the button
        label = gtk.Label(label_text)

        # Pack the pixmap and label into the box
        box.pack_start(image, False, False, 3)
        box.pack_start(label, False, False, 3)

        box.show_all()

        button = gtk.Button()
        button.add(box)
        return button



    @classmethod
    def register_iconsets(cls, icon_info):
        for stock_id, file in icon_info:
            cls.register_iconset(stock_id, file)


    @classmethod
    def register_iconset(cls, stock_id, file):
        if not cls._iconfactory:
            cls._iconfactory = gtk.IconFactory()
            cls._iconfactory.add_default()

        pixbuf = gtk.gdk.pixbuf_new_from_file(file)
        iconset = gtk.IconSet(pixbuf)
        cls._iconfactory.add(stock_id, iconset)



