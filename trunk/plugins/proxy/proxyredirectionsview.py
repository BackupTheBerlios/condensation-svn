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

# no redirect / redirect server domains / redirect all domains
# map domain -> server

import gtk

import condensation

from proxymappingwidget import ProxyMappingWidget

class ProxyRedirectionsView(gtk.VBox):

    def __init__(self, proxy):
        gtk.VBox.__init__(self)

        domains_suggested ={'*': []}
        domain_map = {}

        for server in condensation.Server.servers:
            for vhost in server.vhosts:
                for domain in vhost.domains:
                    if domain not in domains_suggested:
                        domains_suggested[domain] = []
                    domains_suggested[domain].append(vhost)
                    if domain not in domain_map:
                        domain_map[domain] = (False, vhost._server.host)

        if '*' not in domain_map:
            domain_map['*'] = (False, '')

        #print domains_suggested
        #print domain_map


        self.mappingwidget = ProxyMappingWidget(domain_map)
        self.add(self.mappingwidget)



    def get_icon(self):
        return None



    def get_name(self):
        return "Redirections"


