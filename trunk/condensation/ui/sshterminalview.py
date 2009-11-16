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


class SSHTerminalView(gtk.HBox):


    def __init__(self, server):
        # init variables
        gtk.HBox.__init__(self)

        # connection stuff
        self.channel = None
        self.server = server
        self.server.connect_signal('connected', self.on_server_connected)
        self.server.connect_signal('disconnected', self.on_server_disconnected)

        # add/init terminal
        self.terminal =  vte.Terminal()
        self.terminal.connect('commit', self.on_vte_commit)
        self.pack_start(self.terminal, True, True, 0)

        # add scrollbar
        scrollbar = gtk.VScrollbar()
        scrollbar.set_adjustment(self.terminal.get_adjustment())
        self.pack_start(scrollbar, False, False, 0)

        self.show_all()

        if self.server.get_connected():
            self.connect()
        else:
            self.terminal.feed('*** Not connected ***\n\r')



    def connect(self):
        #self.server._transport.set_hexdump(True)
        self.terminal.reset(full=True, clear_history=False)
        self.channel = self.server._transport.open_session()
        self.channel.setblocking(True)
        self.channel.set_combine_stderr(True)
        self.channel.get_pty(term='xterm')
        self.channel.invoke_shell()
        self.running = True
        writer = threading.Thread(target=self.writeall)
        writer.start()
        self.connected = True



    def disconnect(self):
        self.running = False
        self.channel = None # TODO: close channel, if possible
        self.connected = False
        self.terminal.feed('*** disconnected ***\n\r')



    def on_server_connected(self, *args):
        self.connect()



    def on_server_disconnected(self, *args):
        self.disconnect()



    def on_vte_commit(self, widget, text, size):
        #print "Commit '%s' %d" % (text, size)
        if self.channel:
            self.channel.send(text)
        return True



    def writeall(self):
        while self.running:
            data = self.channel.recv(256)
            gtk.gdk.threads_enter()
            if not data:
                #term.feed('\r\n*** EOF ***\r\n\r\n')
                running = False
            else:
                self.terminal.feed(data)
        print "leaving writeall"



