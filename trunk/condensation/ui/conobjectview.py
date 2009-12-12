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

from formwidgetfactory import FormWidgetFactory


class CONObjectView(gtk.Notebook):

    def __init__(self, object):
        gtk.Notebook.__init__(self)
        self.object = object
        self._field_widgets = {} #: the widgets for each field
        self._field_category = {} #: maps the field_id to it's category
        self._category_changed_counter = {} #: number of changed fields in the category
        self._category_apply_buttons = {} # apply buttons for each category
        self._category_reset_buttons = {} # apply buttons for each category

        widgetfactory = FormWidgetFactory()
        for (category_id, category) in enumerate(self.categories):
            self._category_changed_counter[category_id] = 0

            num_rows = len(category[1]) + 1
            table = gtk.Table(rows=num_rows, columns=1, homogeneous=False)
            vbox = gtk.VBox()
            vbox.pack_start(table, expand=False, fill=True, padding=5)
            self.append_page(vbox, gtk.Label(category[0]))

            row = 0
            for (field_id, field_label) in category[1]:
                self._field_category[field_id] = category_id

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
                widget = widgetfactory.create_widget(self.object, field_id)
                widget.connect('changed', self._changed_callback, field_id)

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

            apply_button = gtk.Button(stock=gtk.STOCK_APPLY)
            hbuttonbox.add(apply_button)
            apply_button.connect('clicked', self._apply_callback, category_id)
            self._category_apply_buttons[category_id] = apply_button

            reset_button = gtk.Button(stock=gtk.STOCK_REVERT_TO_SAVED)
            hbuttonbox.add(reset_button)
            reset_button.connect('clicked', self._reset_callback, category_id)
            self._category_reset_buttons[category_id] = reset_button

            self.reset_category(category_id)

        self.show_all()



    def reset_category(self, category_id):
        """
        Reset all field of a category to their start values.
        """
        for (field_id, field_label) in self.categories[category_id][1]:
            self._field_widgets[field_id].reset()

        self._category_changed_counter[category_id] = 0
        self._category_apply_buttons[category_id].set_sensitive(False)
        self._category_reset_buttons[category_id].set_sensitive(False)



    def _apply_callback(self, button, category_id):
        """
        Callback for the apply buttons on each notebook page.
        """
        for (field_id, field_label) in self.categories[category_id][1]:
            self._field_widgets[field_id].apply()

        self._category_changed_counter[category_id] = 0
        self._category_apply_buttons[category_id].set_sensitive(False)
        self._category_reset_buttons[category_id].set_sensitive(False)



    def _reset_callback(self, button, category_id):
        """
        Callback for the reset buttons on each notebook page.
        """
        self.reset_category(category_id)



    def _changed_callback(self, widget, field_id):
        category_id = self._field_category[field_id]

        if self._field_widgets[field_id].is_modified():
            self._category_changed_counter[category_id] += 1
        else:
            self._category_changed_counter[category_id] -= 1

        if self._category_changed_counter[category_id] == 0:
            self._category_apply_buttons[category_id].set_sensitive(False)
            self._category_reset_buttons[category_id].set_sensitive(False)
        else:
            self._category_apply_buttons[category_id].set_sensitive(True)
            self._category_reset_buttons[category_id].set_sensitive(True)

