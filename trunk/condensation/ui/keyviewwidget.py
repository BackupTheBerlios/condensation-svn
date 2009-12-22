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
import md5
import paramiko

class KeyViewWidget(gtk.TreeView):
    """Widget for inspecting a cryptographic key or certificate."""

    def __init__(self, key):
        gtk.TreeView.__init__(self)
        self.key = key

        # print some info about the key
        #print type(key)
        #print dir(key)

        self.cell_name = gtk.CellRendererText()
        self.tvcol_name = gtk.TreeViewColumn(_('Name'))
        self.tvcol_name.pack_start(self.cell_name, True)
        self.tvcol_name.add_attribute(self.cell_name, 'text', 0)

        self.cell_value = gtk.CellRendererText()
        self.tvcol_value = gtk.TreeViewColumn(_('Value'))
        self.tvcol_value.pack_start(self.cell_value, True)
        self.tvcol_value.add_attribute(self.cell_value, 'text', 1)

        self._treestore = gtk.TreeStore(str, str)
        self.set_model(self._treestore)
        self.append_column(self.tvcol_name)
        self.append_column(self.tvcol_value)

        self.set_enable_search(False)
        self.set_headers_visible(True)
        self.set_enable_tree_lines(True)

        if type(key) == paramiko.RSAKey:
            fingerprint = md5.new(str(key)).hexdigest()
            root = self._treestore.append(None, (_('SSH-RSA Key'), fingerprint))
            self._treestore.append(root, (_('Fingerprint'), fingerprint))
            self._treestore.append(root, (_('Size'), str(key.get_bits())))
            self._treestore.append(root, (_('Name'), key.get_name()))
            self._treestore.append(root, (_('Can Sign'), str(key.can_sign())))
        else:
            raise Exception(_('Unknown key type'))







