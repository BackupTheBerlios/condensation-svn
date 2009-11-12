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

import lib.ui


class VHostConfigView(lib.ui.CONObjectView):


    categories = (
        ('General', (
            ('name', 'Name'),
            ('domains', 'Domains'),
            ('document_root', 'Document Root'),
        )),
    )


    def __init__(self, vhost):
        self._vhost = vhost
        lib.ui.CONObjectView.__init__(self)



    def get_field_value(self, field_name):
        #print "Getting %s: %s" % (field_name, str(self.vhost.get_property(field_name)))
        return self._vhost.__getattr__(field_name)



    def get_field_definition(self, field_name):
        return self._vhost.get_attribute_definition(field_name)

