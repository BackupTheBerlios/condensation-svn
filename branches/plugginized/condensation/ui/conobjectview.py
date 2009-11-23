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

from coloredframe import ColoredFrame
from integerlistwidget import IntegerListWidget
from stringlistwidget import StringListWidget


class CONObjectView(gtk.Notebook):

    def __init__(self, object):
        gtk.Notebook.__init__(self)
        self.object = object
        self._start_values = {} #: the initial field values (used by reset)
        self._field_widgets = {} #: the widgets for each field
        self._field_frames = {} #: the frames for each field
        self._field_changed = {} #: wether the field was changed or not
        self._field_category = {} #: maps the field_id to it's category
        self._category_changed_counter = {} #: number of changed fields in the category
        self._category_apply_buttons = {} # apply buttons for each category
        self._category_reset_buttons = {} # apply buttons for each category

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

                # remember the field's current value
                self._start_values[field_id] = self.object.__getattr__(field_id)
                self._field_changed[field_id] = False

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
                definition = self.object.get_attribute_definition(field_id)
                if definition['type'] == 'boolean':
                    widget = gtk.CheckButton()
                    widget.connect('toggled', self._checkbutton_toggled_callback, field_id)
                elif definition['type'] == 'integer[]':
                    widget = IntegerListWidget(definition['min'], definition['max'], self.object.__getattr__(field_id))
                    widget.connect('changed', self._integerlist_changed_callback, field_id)
                elif definition['type'] == 'string':
                    widget = gtk.Entry()
                    widget.connect('changed', self._entry_changed_callback, field_id)
                    widget.set_width_chars(40)
                elif definition['type'] == 'string[]':
                    widget = StringListWidget(self.object.__getattr__(field_id))
                    widget.connect('changed', self._stringlist_changed_callback, field_id)
                else:
                    raise Exception("Unknown type '%s'" % type)

                frame = ColoredFrame()
                frame.add(widget)

                table.attach(frame,
                    left_attach = 1, right_attach = 2, top_attach = row, bottom_attach = row + 1,
                    xoptions=gtk.FILL, yoptions=gtk.EXPAND,
                    xpadding=10, ypadding=0)

                self._field_widgets[field_id] = widget
                self._field_frames[field_id] = frame

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


    def _set_widget_value(self, field_id, value):
        """
        Sets the value in the widget to the one given.
        """
        type = self.object.get_attribute_definition(field_id)['type']
        widget = self._field_widgets[field_id]
        if type == 'boolean':
            widget.set_active(value)
        elif type == 'integer[]':
            widget.set_list(value)
        elif type == 'string':
            text = value
            if text == None:
                text = ''
            widget.set_text(text)
        elif type == 'string[]':
            widget.set_list(value)
        else:
            print "Setting for type '%s' not implemented" % type

        self._set_changed(field_id, value != self._start_values[field_id])



    def _get_widget_value(self, field_id):
        """
        Gets the value from the widget.
        """
        type = self.object.get_attribute_definition(field_id)['type']
        widget = self._field_widgets[field_id]
        if type == 'boolean':
            return widget.get_active()
        elif type == 'integer[]':
            return widget.get_list()
        elif type == 'string':
            return widget.get_text()
        elif type == 'string[]':
            return widget.get_list()
        else:
            print "Getting for type '%s' not implemented" % type



    def reset_category(self, category_id):
        """
        Reset all field of a category to their start values.
        """
        for (field_id, field_label) in self.categories[category_id][1]:
            self._set_widget_value(field_id, self._start_values[field_id])

        self._category_changed_counter[category_id] = 0
        self._category_apply_buttons[category_id].set_sensitive(False)
        self._category_reset_buttons[category_id].set_sensitive(False)



    def _apply_callback(self, button, category_id):
        """
        Callback for the apply buttons on each notebook page.
        """
        self._category_changed_counter[category_id] = 0
        for (field_id, field_label) in self.categories[category_id][1]:
            value = self._get_widget_value(field_id)
            self.object.__setattr__(field_id, value)
            self._set_changed(field_id, False)
            self._start_values[field_id] = value


    def _reset_callback(self, button, category_id):
        """
        Callback for the reset buttons on each notebook page.
        """
        self.reset_category(category_id)



    def _entry_changed_callback(self, entry, field_id):
        """
        Callback for gtk.Entry widgets.
        """
        self._set_changed(field_id, entry.get_text() != self._start_values[field_id])



    def _checkbutton_toggled_callback(self, checkbutton, field_id):
        """
        Callback for gtk.CheckButton widgets.
        """
        self._set_changed(field_id, checkbutton.get_active() != self._start_values[field_id])



    def _integerlist_changed_callback(self, integerlist, field_id):
        """
        Callback for lib.ui.IntegerList widgets.
        """
        self._set_changed(field_id, integerlist.get_list() != list(self._start_values[field_id]))



    def _stringlist_changed_callback(self, stringlist, field_id):
        """
        Callback for lib.ui.StringList widgets.
        """
        self._set_changed(field_id, stringlist.get_list() != list(self._start_values[field_id]))



    def _set_changed(self, field_id, changed):
        """
        Called whenever the changed status of a widget has changed.
        """
        category_id = self._field_category[field_id]
        if self._field_changed[field_id] == changed:
            return # nothing happened ... really

        #print "Setting field '%s' to %s" % (field_id, str(changed))

        if changed:
            self._category_changed_counter[category_id] += 1
            self._field_frames[field_id].set_color('#ff0000')
        else:
            self._category_changed_counter[category_id] -= 1
            self._field_frames[field_id].set_color()

        self._field_changed[field_id] = changed
        if self._category_changed_counter[category_id] == 0:
            self._category_apply_buttons[category_id].set_sensitive(False)
            self._category_reset_buttons[category_id].set_sensitive(False)
        else:
            self._category_apply_buttons[category_id].set_sensitive(True)
            self._category_reset_buttons[category_id].set_sensitive(True)

