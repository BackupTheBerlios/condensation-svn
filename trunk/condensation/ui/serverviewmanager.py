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

import condensation

from keyviewwidget import KeyViewWidget
from resources import Resources
from serverconfigview import ServerConfigView
from textentrydialog import TextEntryDialog
from viewmanager import ViewManager

class ServerViewManager(ViewManager):

    def __init__(self, containing_notebook, view_object):
        ViewManager.__init__(self, containing_notebook, view_object)

        self.view_object.connect_signal('changed', self.on_server_changed)

        # populate toolbar
        self.connect_button = gtk.ToolButton(gtk.STOCK_CONNECT)
        self.connect_button.connect('clicked', self.action_connect)
        self._toolbar.insert(self.connect_button, -1)
        self.connect_button.show()

        self.disconnect_button = gtk.ToolButton(gtk.STOCK_DISCONNECT)
        self.disconnect_button.connect('clicked', self.action_disconnect)
        self._toolbar.insert(self.disconnect_button, -1)
        self.disconnect_button.show()

        self.install_key_button = gtk.ToolButton('condensation-install-key')
        self.install_key_button.connect('clicked', self.action_install_key)
        self._toolbar.insert(self.install_key_button, -1)
        self.install_key_button.show()

        self.update()



    def action_connect(self, action=None):
        while not self.view_object.is_connected():
            try:
                self.view_object.connect_to_server()
            except condensation.PasswordRequiredException, e:
                passwd = TextEntryDialog.run_dialog(
                    _('password required'),
                    _('Please enter your password for user <b>%s</b> on <b>%s</b>') % (self.view_object.ssh_user, self.view_object.host),
                    _('password'),
                    _('The password will <b>not</b> be saved.'),
                    True)
                #TODO: when canceled, return
                self.view_object._ssh_password = passwd
                self.view_object.connect_to_server()
            except condensation.NewServerKeyException, e:
                dialog = gtk.MessageDialog(
                parent=None,
                flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                type=gtk.MESSAGE_WARNING,
                buttons=gtk.BUTTONS_NONE,
                message_format=None)

                dialog.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
                dialog.add_button(gtk.STOCK_SAVE, gtk.RESPONSE_ACCEPT)

                dialog.set_title(_('Unknown Key - %s') % self.view_object.host)
                dialog.set_markup(_('There is no known key for the host %s, please ensure that the key presented below belongs to that host.') % self.view_object.host)
                dialog.format_secondary_markup(_('The key will be saved to ensure the host\'s identity in the future.'))

                keyview = KeyViewWidget(e.new_key)
                dialog.vbox.pack_end(keyview, True, True, 0)
                dialog.vbox.show_all()

                response = dialog.run()
                dialog.destroy()
                if response == gtk.RESPONSE_ACCEPT:
                    self.view_object.ssh_key_fingerprint = md5.new(str(e.new_key)).hexdigest()
                else:
                    return



    def action_disconnect(self, action=None):
        self.view_object.disconnect()


    def action_install_key(self, action=None):
        self.view_object.install_auth_key()


    def on_server_changed(self, server):
        self.update()



    def update(self):
        self.connect_button.set_property('sensitive', not self.view_object.is_connected())
        self.disconnect_button.set_property('sensitive', self.view_object.is_connected())


    def get_menu_text(self):
        return self.view_object.name



    def get_menu_icon(self):
        if self.view_object.is_connected():
            return 'condensation-server-connected'
        else:
            return 'condensation-server-disconnected'


