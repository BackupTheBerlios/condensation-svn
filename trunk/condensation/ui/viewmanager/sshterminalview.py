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
        # Set up terminal
        gtk.HBox.__init__(self)
        self.terminal =  vte.Terminal()
        self.pack_start(self.terminal, True, True, 0)

        # add scrollbar
        scrollbar = gtk.VScrollbar()
        scrollbar.set_adjustment(self.terminal.get_adjustment())
        self.pack_start(scrollbar, False, False, 0)

        self.show_all()

        # wire channel to terminal
        self.server = server
        if self.server.get_connected():
            self.connect()
        else:
            self.terminal.feed('Not connected\n\r')


    def connect(self):
        #self.server._transport.set_hexdump(True)
        self.channel = self.server._transport.open_session()
        self.channel.setblocking(True)
        self.channel.set_combine_stderr(True)
        self.channel.get_pty(term='xterm')
        self.channel.invoke_shell()
        self.terminal.connect('commit', self.on_commit)
        writer = threading.Thread(target=self.writeall)
        writer.start()



    def on_commit(self, widget, text, size):
        #print "Commit '%s' %d" % (text, size)
        self.channel.send(text)
        return True



    def writeall(self):
        running = True
        while running:
            data = self.channel.recv(256)
            gtk.gdk.threads_enter()
            if not data:
                #term.feed('\r\n*** EOF ***\r\n\r\n')
                running = False
            else:
                self.terminal.feed(data)
        print "leaving writeall"



