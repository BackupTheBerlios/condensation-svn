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

from stringlistwidget import StringListWidget


class CONObjectView(gtk.Notebook):

    def __init__(self):
        gtk.Notebook.__init__(self)
        self._start_values = {} #: the initial field values (used by reset)
        self._field_widgets = {} #: the widgets for each field

        for (category_id, category) in enumerate(self.categories):
            num_rows = len(category[1]) + 1
            table = gtk.Table(rows=num_rows, columns=1, homogeneous=False)
            vbox = gtk.VBox()
            vbox.pack_start(table, expand=False, fill=True, padding=5)
            self.append_page(vbox, gtk.Label(category[0]))

            row = 0
            for (field_id, field_label) in category[1]:
                # remember the field's current value
                self._start_values[field_id] = self.get_field_value(field_id)

                # create the label
                label = gtk.Label()
                label.set_markup("<b>"+field_label+":</b>")
                label.set_justify(gtk.JUSTIFY_LEFT)
                label.set_alignment(0.0, 0.0)
                table.attach(label,
                    left_attach = 0, right_attach = 1, top_attach = row, bottom_attach = row + 1,
                    xoptions=gtk.FILL, yoptions=gtk.EXPAND | gtk.FILL,
                    xpadding=10, ypadding=7)

                # now, on to the field itself
                type = self.get_field_type(field_id)
                if type == 'boolean':
                    widget = gtk.CheckButton()
                elif type == 'integer[]':
                    widget = gtk.Label('type integer[] not implemented yet')
                elif type == 'string':
                    widget = gtk.Entry()
                    widget.connect('changed', self._entry_changed_callback, field_id)
                    widget.set_width_chars(40)
                elif type == 'string[]':
                    widget = StringListWidget(self.get_field_value(field_id))
                else:
                    raise Exception("Unknown type '%s'" % type)


                table.attach(widget,
                    left_attach = 1, right_attach = 2, top_attach = row, bottom_attach = row + 1,
                    xoptions=gtk.FILL, yoptions=gtk.EXPAND,
                    xpadding=10, ypadding=0)

                self._field_widgets[field_id] = widget

                row += 1

            # build reset and apply buttons
            hbuttonbox = gtk.HButtonBox()
            hbuttonbox.set_layout(gtk.BUTTONBOX_END)
            hbuttonbox.set_spacing(20)
            vbox.pack_end(hbuttonbox, expand=False, fill=False, padding=5)

            applyb = gtk.Button(stock=gtk.STOCK_APPLY)
            hbuttonbox.add(applyb)

            resetb = gtk.Button(stock=gtk.STOCK_REVERT_TO_SAVED)
            hbuttonbox.add(resetb)
            resetb.connect('clicked', self._reset_callback, category_id)

            self.reset_category(category_id)

        self.show_all()



    def reset_category(self, category_id):
        """
        Reset all field of a category to their start values.
        """
        for (field_id, field_label) in self.categories[category_id][1]:
            type = self.get_field_type(field_id)
            widget = self._field_widgets[field_id]
            if type == 'boolean':
                pass
            elif type == 'string':
                text = self._start_values[field_id]
                if text == None:
                    text = ''
                widget.set_text(text)
            elif type == 'string[]':
                pass



    def _reset_callback(self, button, category_id):
        """
        Callback for the reset buttons on each notebook page.
        """
        self.reset_category(category_id)



    def _entry_changed_callback(self, entry, field_id):
        """
        Callback for the changed signal of entry widgets.
        """
        if entry.get_text() == self._start_values[field_id]:
            entry.modify_bg(gtk.STATE_NORMAL, gtk.widget_get_default_style().bg_gc[gtk.STATE_NORMAL])
        else:
            entry.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#ff0000'))



    def get_field_value(self, field_name):
        """
        Return the content for the form field.

        Must be implemented by subclasses.
        """
        raise Exception("Not Implemented!")



    def get_field_type(self, field_name):
        """
        Return the type of the field (see `DAObject` for property types).

        Must be implemented by subclasses.
        """
        raise Exception("Not Implemented!")

