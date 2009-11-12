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


from key import Key
import lib.core


class KeyManager(lib.core.CONBorg):

    _attribute_definitions = (
        {'name': 'ssh_auth_key', 'type':'Key', 'default':None},
    )
    _signal_list = (())


    def __init__(self):
        lib.core.CONBorg.__init__(self)



    def get_ssh_auth_key(self):
        if self.ssh_auth_key == None:
            print "generating new key"
            new_key = Key.generate_rsa_key(4096)
            self.ssh_auth_key = new_key
        return self.ssh_auth_key




lib.core.CONObject.register_attribute_type('KeyManager', KeyManager.object_serializer, KeyManager.object_deserializer)
