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

from baseformwidget import BaseFormWidget
from integerlistwidget import IntegerListWidget

class IntegerListFormWidget(BaseFormWidget):

    def __init__(self, conobj, attr):
        BaseFormWidget.__init__(self, conobj, attr)
        definition = self._conobj.get_attribute_definition(attr)
        self._widget = IntegerListWidget(definition['min'], definition['max'], self._start_value)
        self._widget.connect('changed', self._changed_callback)
        self.add(self._widget)


    def _get_value(self):
        return self._widget.get_list()


    def _set_value(self, value):
        self._widget.set_list(value)


    def _changed_callback(self, stringlist):
        self._update_modified()
