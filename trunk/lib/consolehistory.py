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


class ConsoleHistory(object):
    def __init__(self):
        object.__init__(self)
        self.items = ['']
        self.ptr = 0
        self.edited = {}


    def commit(self, text):
        if text:
            self.items[-1] = text
            self.items.append('')
        self.ptr = len(self.items) - 1
        self.edited = {}


    def get(self, dir, text):
        #print "get(self, %d, %s) [ptr=%d]" % (dir, text, self.ptr)
        if len(self.items) == 1:
            return None

        if text != self.items[self.ptr]:
            self.edited[self.ptr] = text
        elif self.ptr in self.edited:
            del self.edited[self.ptr]

        self.ptr = self.ptr + dir
        if self.ptr >= len(self.items):
            self.ptr = len(self.items) - 1
        elif self.ptr < 0:
            self.ptr = 0

        if self.ptr in self.edited:
            return self.edited[self.ptr]
        else:
            return self.items[self.ptr]
