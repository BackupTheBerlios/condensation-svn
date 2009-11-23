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


import string
import random


class Util(object):

    @classmethod
    def commonprefix(cls, m):
        "Given a list of pathnames, returns the longest common leading component"
        if not m: return ''
        prefix = m[0]
        for item in m:
            for i in range(len(prefix)):
                if prefix[:i+1] != item[:i+1]:
                    prefix = prefix[:i]
                    if i == 0:
                        return ''
                    break
        return prefix



    @classmethod
    def random_string(cls, length):
        chars = string.ascii_letters + string.digits
        s = ''
        for x in xrange(length):
            s += random.choice(chars)
        return s



    @classmethod
    def random_integer(cls, min, max):
        return random.randint(min, max)

