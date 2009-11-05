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

import paramiko
import OpenSSL.crypto
import xml.etree.ElementTree as ET
from StringIO import StringIO


import lib.core


class Key(lib.core.CONObject):


    def __init__(self):
        lib.core.CONObject.__init__(self)



    def get_authorized_keys_line(self):
        """
        Creates a line suitable for adding the key to the authorized_keys file.
        """
        if self._type == 'ssh-rsa':
            line = 'ssh-rsa '
            line += self._key.get_base64()
            line += " Key added by DrupalAdmin\n"
        else:
            raise Exception("Unsupported key type")
        return line



    @classmethod
    def generate_ssh_rsa_key(cls, bits=4096):
        key = DAKey()
        key._key = paramiko.RSAKey.generate(bits)
        key._type = 'ssh-rsa'
        return key



    @classmethod
    def generate_ssl_rsa_key(cls, bits=4096):
        key = DAKey()
        key._key = OpenSSL.crypto.PKey()
        key._key.generate_key(OpenSSL.crypto.TYPE_RSA, bits)
        key._type = 'ssl-rsa'
        return key



    @classmethod
    def key_serializer(cls, element, value):
        """
        Serializer function used by DAObject's serializing mechanism for serializing DAObject-objects.

        :param element: the ElementTree element which will contain the serialized data
        :param value: the value (ie the DAObject-object) to be serialized
        """
        # if value is None keep the element empty
        if value == None:
            return
        element.text = "\n"
        type_elem = ET.SubElement(element, 'type')
        type_elem.text = value._type
        type_elem.tail = "\n"

        strio = StringIO()
        value._key.write_private_key(strio)
        data_elem = ET.SubElement(element, 'data')
        data_elem.text = strio.getvalue()
        data_elem.tail = "\n"
        strio.close()



    @classmethod
    def key_deserializer(cls, et):
        """
        Deserializer function used by DAObject's serializing mechanism for deserializing DAObject-objects.

        :param et: the ElementTree containing the serialized object properties
        """
        dakey = cls()
        type_elem = et.find('type')
        dakey._type = type_elem.text
        if dakey._type == 'ssh-rsa':
            data_elem = et.find('data')
            strio = StringIO(data_elem.text)
            dakey._key = paramiko.RSAKey(file_obj=strio)
            strio.close()
        else:
            raise Exception('Unknown key-type %s' % dakey._type)
        return dakey




lib.core.CONObject.register_attribute_type('Key', Key.key_serializer, Key.key_deserializer)

lib.core.CONObject.register_class(Key, (()), (()))