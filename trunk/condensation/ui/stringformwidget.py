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

from baseformwidget import BaseFormWidget

class StringFormWidget(BaseFormWidget):

    def __init__(self, conobj, attr):
        BaseFormWidget.__init__(self, conobj, attr)
        self._widget = gtk.Entry()
        self._widget.connect('changed', self._entry_changed_callback)
        self._widget.set_width_chars(40)
        self.add(self._widget)


    @classmethod
    def can_handle(cls, attribute_definition):
        return attribute_definition['type'] == 'string'


    def _get_value(self):
        return self._widget.get_text()


    def _set_value(self, value):
        self._widget.set_text(value)


    def _entry_changed_callback(self, entry):
        self._update_modified()
