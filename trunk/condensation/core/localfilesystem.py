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


import os
import os.path

from filesystem import FileSystem


class LocalFileSystem(FileSystem):

    def __init__(self):
        self.path_separator = '/'
        self.home_dir = '/' # TODO: set home dir


    def exists(self, path):
        """
        See `DAFileSystem.exists`.
        """
        return os.path.exists(self.construct_path(path))



    def listdir(self, path):
        """
        See `DAFileSystem.listdir`.
        """
        return os.listdir(self.construct_path(path))



    def open(self, path, mode="r"):
        """
        See `DAFileSystem.open`.
        """
        return open(self.construct_path(path), mode)



    def mkdir(self, path):
        """
        See `DAFileSystem.mkdir`.
        """
        return os.mkdir(self.construct_path(path))


