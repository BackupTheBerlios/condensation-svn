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

import logging
import os
import sys

import condensation.core

class PluginManager(condensation.core.CONBorg):


    _attribute_definitions = []
    _signal_list = (())
    _plugin_modules = []


    def __init__(self):
        condensation.core.CONBorg.__init__(self)



    def load_plugins(self):
        for cname in os.listdir('plugins'):
            path = os.path.abspath('plugins/'+cname)
            if not os.path.isdir(path):
                continue
            if cname == '.svn':
                continue
            package_name = 'plugins.'+cname
            if package_name in sys.modules:
                print "Skipping already loaded plugin %s." % cname
            else:
                __import__(package_name)
            self.install_plugin(sys.modules[package_name])



    def install_plugin(self, module):
        logger = logging.getLogger('PluginManager')
        logger.info("installing plugin '%s'" % module.__plugin_name__)
        self._plugin_modules.append(module)
        if '__install_plugin__' not in module.__dict__:
            logger.error("plugin %s is missing the __install_plugin__() function" % module.__plugin_name__)
            return
        module.__install_plugin__()



    def cleanup_plugins(self):
        logger = logging.getLogger('PluginManager')
        for module in self._plugin_modules:
            if '__cleanup_plugin__' in module.__dict__:
                logger.info("cleaning up for plugin '%s'" % module.__plugin_name__)
                module.__cleanup_plugin__()

