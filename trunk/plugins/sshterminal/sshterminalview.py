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


import vte
import gtk.gdk
import gtk
import threading

import condensation.ui

class SSHTerminalView(gtk.HBox):


    def __init__(self, server):
        # init variables
        gtk.HBox.__init__(self)

        # define actions
        self._menuitems = [
            ('_Copy', self._copy),
            ('_Paste', self._paste),
        ]

        # connection stuff
        self.connected = False
        self.channel = None
        self.server = server
        self.server.connect_signal('connected', self._server_connected)
        self.server.connect_signal('disconnected', self._server_disconnected)

        # add/init terminal
        self.terminal =  vte.Terminal()
        self.terminal.connect('commit', self._vte_commit)
        self.terminal.connect('size-allocate', self._size_allocate)
        self.terminal.connect('button-press-event', self._button_press)
        self.terminal.connect('key-press-event', self._key_press)
        self.pack_start(self.terminal, True, True, 0)

        # add scrollbar
        scrollbar = gtk.VScrollbar()
        scrollbar.set_adjustment(self.terminal.get_adjustment())
        self.pack_start(scrollbar, False, False, 0)

        self.show_all()


        if self.server.is_connected():
            self.connect()
        else:
            self.terminal.feed('*** Not connected ***\n\r')


    def get_icon(self):
        return 'condensation-ssh-terminal-icon'



    def get_name(self):
        return "SSH Terminal"



    def connect(self):
        #self.server._transport.set_hexdump(True)
        self.terminal.reset(full=True, clear_history=False)
        self.channel = self.server._transport.open_session()
        self.channel.setblocking(True)
        self.channel.set_combine_stderr(True)
        self.channel.get_pty(
            term='xterm',
            width=self.terminal.get_column_count(),
            height=self.terminal.get_row_count()
        )
        self.channel.invoke_shell()
        self.running = True
        writer = threading.Thread(target=self._writeall)
        writer.start()
        self.connected = True



    def disconnect(self):
        self.running = False
        self.channel = None # TODO: close channel, if possible
        self.connected = False
        self.terminal.feed('\n\r*** disconnected ***\n\r')



    def _server_connected(self, *args):
        self.connect()



    def _server_disconnected(self, *args):
        self.disconnect()



    def _vte_commit(self, widget, text, size):
        #print "Commit '%s' %d" % (text, size)
        if self.channel:
            self.channel.send(text)
        return True



    def _writeall(self):
        while self.running:
            data = self.channel.recv(256)
            gtk.gdk.threads_enter()
            if not data:
                #term.feed('\r\n*** EOF ***\r\n\r\n')
                running = False
            else:
                self.terminal.feed(data)



    def _size_allocate(self, widget, allocation):
        if self.connected:
            self.channel.resize_pty(
                width=self.terminal.get_column_count(),
                height=self.terminal.get_row_count()
            )



    def _copy(self, event=None):
        self.terminal.copy_clipboard()



    def _paste(self, event=None):
        self.terminal.paste_clipboard()



    def _button_press(self, term, event):
        if event.button == 3:
            menu = gtk.Menu()

            for itemdef in self._menuitems:
                menuitem =  gtk.MenuItem(itemdef[0], True)
                menuitem.connect('activate', itemdef[1])
                menu.append(menuitem)

            menu.show_all()
            menu.popup(None, None, None, event.button, event.time)
            return True
        return False



    def _key_press(self, term, event):
        mask = gtk.gdk.SHIFT_MASK | gtk.gdk.CONTROL_MASK
        if event.state & mask == mask:
            if event.keyval == ord('C'):
                self._copy()
            elif event.keyval == ord('V'):
                self._paste()
            return True
        return False

