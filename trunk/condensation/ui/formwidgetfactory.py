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

from booleanformwidget import BooleanFormWidget
from integerlistformwidget import IntegerListFormWidget
from stringformwidget import StringFormWidget
from stringlistformwidget import StringListFormWidget

class FormWidgetFactory(object):

    _registry = []

    def __init__(self):
        pass


    def create_widget(self, conobj, attr):
        definition = conobj.get_attribute_definition(attr)
        for widget in self._registry:
            if widget.can_handle(definition):
                return widget(conobj, attr)
        raise Exception("Found no widget to handle attribute with definition "+str(definition))



    @classmethod
    def register_widget(cls, widget):
        cls._registry.append(widget)
