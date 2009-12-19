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

import uuid
import xml.etree.ElementTree as ET

from conobject import CONObject



class CONBorg(CONObject):
    """
    This class provides a borg pattern for CONObjects.

    The borg pattern is similar to the singleton pattern in that it provides access
    to a single data set. unlike a singleton where there is only one object instance,
    in the borg pattern each object shares the same data.
    """

    _attribute_definitions = (())
    _signal_list = (())


    def __init__(self):
        """
        Initializes variables and registers the 'attribute_changed' signal.

        It is neccessary for each subclass to call CONObject's __init__, failing to do so
        will prevent the subclass to use signals and attributes.
        """
        # register our class, if not registered before
        if self.__class__ not in CONObject._class_registry:
            CONObject._register_class(self.__class__)

        # init signal callback lists
        if '_callbacks' not in self.__class__.__dict__:
            self.__class__._callbacks = {}
            for signal in CONObject._class_registry[self.__class__]['callbacks']:
                self.__class__._callbacks[signal] = []

        # init attribute list
        if '_attributes' not in self.__class__.__dict__:
            self.__class__._attributes = CONObject._class_registry[self.__class__]['attributes'].copy()



    def connect_signal(self, signal, callback):
        """
        Connect a signal to a callback. One signal can have multiple callbacks (or none at all).

        :param signal: signal identifier
        :param callback: the callback
        """
        if signal not in self.__class__._callbacks:
            raise Exception(_("Can not connect unregistered signal '%s'.") % signal)
        self.__class__._callbacks[signal].append(callback)



    def raise_signal(self, signal, *args):
        """
        Raises a signal, ie. calling all callbacks connected to this signal.

        :param signal: signal identifier
        :param args: variable list of arguments for the callback(s)
        """
        for callback in self.__class__._callbacks[signal]:
            callback(self, *args)



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
            #attribute, check stuff, todo
            if name not in self.__class__._attributes:
                raise Exception(_("Attribute '%s' doesn't exist and therefore can't be set.") % name)

            oldvalue = self.__class__._attributes[name]
            self.__class__._attributes[name] = value

            # try calling any _on_..._changed method
            mname = '_on_'+name+'_changed'
            if hasattr(self, mname):
                method = getattr(self, mname)
                method(oldvalue, value)

            self.raise_signal('attribute_changed', name, oldvalue, value)



    def __getattr__(self, name):
        """
        Return the value of the attribute.

        When the object's uuid is requested but the object has no uuid yet, the uuid is created.
        """
        if name[0:1] == '_':
            return self.__class__.__dict__[name]
        else:
            if (name == 'uuid') and (self.__class__.__dict__['_attributes']['uuid'] == None):
                self.__class__.__dict__['_attributes']['uuid'] = uuid.uuid4()
            return self.__class__.__dict__['_attributes'][name]



    def get_attribute_list(self):
        """
        Returns the list of attributes that are managed by CONObject.
        """
        return self.__class__._attributes.keys()



CONObject.register_attribute_type('CONBorg', CONBorg.object_serializer, CONBorg.object_deserializer)


