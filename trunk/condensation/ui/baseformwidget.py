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

import gobject

from coloredframe import ColoredFrame

class BaseFormWidget(ColoredFrame):


    def __init__(self, conobj, attr):
        ColoredFrame.__init__(self)
        self._conobj = conobj
        self._attr = attr
        self._start_value = self._conobj.__getattr__(self._attr)
        self._modified = False


    @classmethod
    def can_handle(cls, attribute_definition):
        """
        Check wether the class can handle a attribute with the given
        definition or not.
        """
        raise Exception('Not implemented!')


    def _get_value(self):
        """
        Get the widget's value.
        """
        raise Exception('Not implemented!')


    def _set_value(self, value):
        """
        Set the widget's value.
        """
        raise Exception('Not implemented!')


    def apply(self):
        value = self._get_value()
        self._conobj.__setattr__(self._attr, value)
        self._start_value = value
        self._update_modified()


    def reset(self):
        self._set_value(self._start_value)
        self._update_modified()


    def _update_modified(self):
        old_modified = self._modified
        if self._get_value() == self._start_value:
            self._modified = False
            self.set_color()
        else:
            self._modified = True
            self.set_color('#ff0000')

        if self._modified != old_modified:
            self.emit('changed')


    def is_modified(self):
        return self._modified


# register signal 'changed' with gobject
gobject.type_register(BaseFormWidget)
gobject.signal_new('changed', BaseFormWidget, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())
