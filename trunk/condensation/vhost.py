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

from apacheconfigparser import ApacheConfigParser
from core.daobject import DAObject


class VHost(DAObject):


    def __init__(self):
        DAObject.__init__(self)
        self._server = None



    def read_config(self):
        fs = self._server.get_sftp_filesystem()
        self._raw_config = fs.read_file((self._server.apache_available, self.name))
        self._config = ApacheConfigParser.parse_string(self._raw_config)
        #self.config.print_r()



    def install_drupal(self, package):
        if not package.isDrupal():
            raise Exception("Only Drupal packages allowed here")
        package.extract(self._install_callback)



    def _install_callback(self):
        pass



DAObject.register_attribute_type('da.VHost', VHost.daobject_serializer, VHost.daobject_deserializer)

DAObject.register_class(VHost,
    (
        ('name', 'string', ''),
        ('domains', 'string[]', ["test.com", "test2.com", "test3.com"]),
        ('document_root', 'string', '/var/www'),
    ),
    (())
)