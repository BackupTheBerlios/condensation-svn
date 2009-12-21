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

from conobjectview import CONObjectView
from resources import Resources

class ServerConfigView(CONObjectView):

    categories = [
        [_('General'), [
            ('name', _('Name')),
            ('host', _('Host')),
        ]],
        [_('SSH'), [
            ('ssh_port', _('Port')),
            ('ssh_user', _('User')),
            ('ssh_key_fingerprint', _('Key Fingerprint')),
            ('ssh_autoconnect', _('Auto Connect')),
        ]],
        [_('Apache'), [
            ('apache_base', _('Base dir')),
            ('apache_confbase', _('Config dir')),
            ('apache_available', _('Available vhosts')),
            ('apache_enabled', _('Enabled vhosts')),
            ('apache_user', _('User')),
            ('apache_group', _('Group')),
        ]],
        [_('Drupal'), [
            ('drupal_cronfile', _('Cronfile')),
        ]],
        [_('MySQL'), [
            ('mysql_host', _('Server host')),
            ('mysql_user', _('Adminstrative user')),
            ('mysql_password', _('Adminstrative password')),
        ]],
    ]



    def get_icon(self):
        return 'condensation-configuration'



    def get_name(self):
        return self.object.name

