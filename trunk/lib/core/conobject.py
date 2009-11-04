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

import xml.etree.ElementTree as ET
import re


#from concollection import CONCollection
from signalsource import SignalSource


class CONObject(SignalSource):
    """
    Base class for all CON... classes.

    Provides functions for signals (`register_signal`, `connect_signal` and
    `raise_signal`) and attributes (`set_attribute` and `get_attribute`)
    """

    #: list of known attributes
    _attribute_type_registry = {}


    #: list of registered classes
    _class_registry = {}


    _re_collection = re.compile('(?P<basetype>[^\[]+)(\[(?P<indices>[^\]]*)])?$')


    def __init__(self):
        """
        Initializes variables and registers the 'attribute_changed' signal.

        It is neccessary for each subclass to call CONObject's __init__, failing to do so
        will prevent the subclass to use signals and attributes.
        """
        SignalSource.__init__(self)
        for signal in CONObject._class_registry[self.__class__]['callbacks']:
            self.__dict__['_callbacks'][signal] = []
        self.__dict__['_attributes'] = CONObject._class_registry[self.__class__]['attributes'].copy()



    def __setattr__(self, name, value):
        """
        Sets an object-attribute to the given value and fires a attribute_changed signal.

        If the attribute does not exist and does not start with a '_' (underscore) an Exception is raised

        :todo: check type constraints

        :param name: attribute identifier
        :param value: the new value
        """
        if name[0:1] == '_':
            #this is something private, no checking done
            self.__dict__[name] = value
        else:
            #daobject attribute, check stuff
            if name not in self._attributes:
                raise Exception("Attribute '%s' doesn't exist and therefore can't be set." % name)

            oldvalue = self._attributes[name]
            self._attributes[name] = value
            self.raise_signal('attribute_changed', name, oldvalue, value)



    def __getattr__(self, name):
        """
        """
        return self.__dict__['_attributes'][name]



    def get_attribute_type(self, name):
        """
        Returns the type of an object-attribute.

        :param attribute: attribute identifier
        """
        #return self._attributes_type[name]
        return CONObject._class_registry[self.__class__]['attributes_type'][name]



    def get_attribute_list(self):
        return self._attributes.keys()



    def wakeup(self):
        """
        Method gets called after deserialization.
        """
        pass



    @classmethod
    def register_attribute_type(cls, type, serializer, deserializer):
        """
        Register a attribute-type alang with it's serializer and deserializer functions.

        :param type: type identifier
        :param serializer: serializer function
        :param deserializer: deserializer function
        """
        cls._attribute_type_registry[type] = (serializer, deserializer)



    @classmethod
    def register_class(cls, class_obj, attributes, signals):
        if class_obj in cls._class_registry:
            raise Exception('Class already registered')

        eff_attributes = {}
        eff_attributes_type = {}
        eff_callbacks = set()

        for base in class_obj.__bases__:
            if base in cls._class_registry:
                eff_attributes.update(cls._class_registry[base]['attributes'])
                eff_attributes_type.update(cls._class_registry[base]['attributes_type'])
                eff_callbacks.update(cls._class_registry[base]['callbacks'])


        for (name, type, value) in attributes:
            if not isinstance(type, basestring):
                #print CONObject._attribute_type_registry
                raise Exception('String expected here, got %s' % type.__class__)

            m = cls._re_collection.match(type)
            basetype = m.group('basetype')

            if basetype not in cls._attribute_type_registry:
                #print cls._attribute_type_registry
                raise Exception("Cannot init attribute of unregistered type '%s'." % basetype)

            if m.group('indices') != None:
                value = cls._construct_collection(basetype, [], value)

            if name not in eff_attributes:
                eff_attributes[name] = value
                eff_attributes_type[name] = type
            else:
                raise Exception("tried to initialize the existing attribute '%s'." % name)

        for name in signals:
            if name in eff_callbacks:
                raise Exception("Already in list")
            eff_callbacks.add(name)


        cls._class_registry[class_obj] = {
            'attributes': eff_attributes,
            'attributes_type': eff_attributes_type,
            'callbacks': eff_callbacks,
        }



    @classmethod
    def _construct_collection(cls, basetype, indices=[], value=[]):
        collection = DACollection(basetype)
        for index in indices:
            pass

        for val in value:
            collection.add(val)
        return collection



    @classmethod
    def boolean_serializer(cls, element, value):
        """
        Serializer function used by CONObject's serializing mechanism for serializing boolean values.

        :param element: the ElementTree element which will contain the serialized data
        :param value: the value (ie the string) to be serialized
        """
        if value:
            element.text = 'true'
        else:
            element.text = 'false'



    @classmethod
    def boolean_deserializer(cls, element):
        """
        Deserializer function used by CONObject's serializing mechanism for deserializing boolean values.

        :param element: the ElementTree containing the serialized boolean value
        """
        t = element.text.lower()
        if t == 'true' or t == '1' or t == 'on':
            return True
        else:
            return False



    @classmethod
    def integer_serializer(cls, element, value):
        """
        Serializer function used by CONObject's serializing mechanism for serializing integers.

        :param element: the ElementTree element which will contain the serialized data
        :param value: the value (ie the integer) to be serialized
        """
        element.text = value



    @classmethod
    def integer_deserializer(cls, element):
        """
        Deserializer function used by CONObject's serializing mechanism for deserializing integers.

        :param element: the ElementTree containing the serialized integer
        """
        return int(element.text)



    @classmethod
    def string_serializer(cls, element, value):
        """
        Serializer function used by CONObject's serializing mechanism for serializing strings.

        :param element: the ElementTree element which will contain the serialized data
        :param value: the value (ie the string) to be serialized
        """
        element.text = value



    @classmethod
    def string_deserializer(cls, element):
        """
        Deserializer function used by CONObject's serializing mechanism for deserializing strings.

        :param element: the ElementTree containing the serialized string
        """
        if not element.text:
            return '' # prevent None
        else:
            return element.text



    @classmethod
    def daobject_serializer(cls, element, value):
        """
        Serializer function used by CONObject's serializing mechanism for serializing CONObject-objects.

        :param element: the ElementTree element which will contain the serialized data
        :param value: the value (ie the CONObject-object) to be serialized
        """
        # if value is None keep the element empty
        if value == None:
            return
        element.text = "\n"
        names = value.get_attribute_list()
        names.sort()
        for name in names:
            subelement = ET.SubElement(element, name)
            subelement.tail = "\n"
            attr_val = value.__getattr__(name)
            m = cls._re_collection.match(value.get_attribute_type(name))
            if m.group('indices') != None:
                if attr_val != None:
                    basetype = m.group('basetype')
                    subelement.text = "\n"
                    for item in attr_val:
                        itemelement = ET.SubElement(subelement, 'item')
                        itemelement.tail = "\n"
                        CONObject._attribute_type_registry[basetype][0](itemelement, item)
            else:
                CONObject._attribute_type_registry[type][0](subelement, attr_val)



    @classmethod
    def daobject_deserializer(cls, et):
        """
        Deserializer function used by CONObject's serializing mechanism for deserializing CONObject-objects.

        :param et: the ElementTree containing the serialized object attributes
        """
        daobj = cls()
        attr_list = daobj.get_attribute_list()
        for element in et:
            name = element.tag
            if name not in attr_list:
                raise Exception("No object attribute of name '%s'." % name)

            type = daobj.get_attribute_type(name)
            if not isinstance(type, basestring):
                raise Exception('String expected here, got %s' % type.__class__)

            m = cls._re_collection.match(type)
            if m.group('indices') != None:
                basetype = m.group('basetype')
                list = []
                for subelement in element:
                    subvalue = CONObject._attribute_type_registry[basetype][1](subelement)
                    list.append(subvalue)
                daobj.__setattr__(name, list)
            else:
                value = CONObject._attribute_type_registry[type][1](element)
                daobj.__setattr__(name, value)

        daobj.wakeup()
        return daobj





CONObject.register_attribute_type('boolean', CONObject.boolean_serializer, CONObject.boolean_deserializer)
CONObject.register_attribute_type('integer', CONObject.integer_serializer, CONObject.integer_deserializer)
CONObject.register_attribute_type('string', CONObject.string_serializer, CONObject.string_deserializer)
CONObject.register_attribute_type('CONObject', CONObject.daobject_serializer, CONObject.daobject_deserializer)

CONObject.register_class(CONObject, (()), ('attribute_changed',))


