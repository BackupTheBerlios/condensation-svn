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


class ServerConfigView(lib.ui.CONObjectView):

    categories = (
        ('General', (
            ('name', 'Name'),
            ('host', 'Host'),
        )),
        ('SSH', (
            ('ssh_port', 'Port'),
            ('ssh_user', 'User'),
            ('ssh_key_fingerprint', 'Key Fingerprint'),
            ('ssh_autoconnect', 'Auto Connect'),
        )),
        ('Apache', (
            ('apache_base', 'Base dir'),
            ('apache_confbase', 'Config dir'),
            ('apache_available', 'Available vhosts'),
            ('apache_enabled', 'Enabled vhosts'),
            ('apache_user', 'User'),
            ('apache_group', 'Group'),
        )),
        ('Drupal', (
            ('drupal_cronfile', 'Cronfile'),
        )),
        ('MySQL', (
            ('mysql_host', 'Server host'),
            ('mysql_user', 'Adminstrative user'),
            ('mysql_password', 'Adminstrative password'),
        )),
    )


