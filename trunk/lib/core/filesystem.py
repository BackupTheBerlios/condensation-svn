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


class FileSystem(object):
    """
    Base-class for all classes supporting filesystem functions. See `da.core.DALocalFileSystem` for one
    such class.
    """

    def exists(self, path):
        """
        Check if there exists an element given by the path (may be a directory, a file, a link or something else).

        Needs to be implemented in subclasses.

        :param path: file path as in `construct_path`
        """
        raise Exception("Not implemented")



    def listdir(self, path):
        """
        List the dir given by the path elements. See `construct_path` for how the path is constructed.

        Needs to be implemented in subclasses.

        :param path: file path as in `construct_path`
        """
        raise Exception("Not implemented")



    def open(self, path, mode="r"):
        """
        Opens a file given by the path elements. See `construct_path` for how the path is constructed.

        The mode indicates how the file is to be opened: 'r' for reading, 'w' for writing
        (truncating an existing file), 'a' for appending, 'r+' for reading/writing, 'w+' for
        reading/writing (truncating an existing file), 'a+' for reading/appending.

        Needs to be implemented in subclasses.

        :param path: file path as in `construct_path`
        :param mode: mode for opening the file
        """
        raise Exception("Not implemented")



    def mkdir(self, path):
        """
        Creates the dir given by the path elements. See `construct_path` for how the path is constructed.

        Needs to be implemented in subclasses.

        :todo: add mode parameter
        """
        raise Exception("Not implemented")



    def read_file(self, path):
        """
        Read the file given by the path elements. See `construct_path` for how the path is constructed.

        This method opens a file via `open` (mode 'r'), reads it's contents, closes it and returns the content.
        Subclasses should not need to override it.
        """
        realpath = self.construct_path(path)
        self._logger.debug("SFTP-FS : read_file %s" % realpath)
        file = self.sftp_client.file(realpath, mode="r")
        string = file.read()
        file.close()
        return string



    def construct_path(self, path):
        """
        Construct a path out of the path(-elements) given.

        When path is a string, this string is returned (it might be normalized though).

        If the path is a squence, it's elements are joined together using pathseperator.

        Additionally all occurences of '~' are replaced with the user's homedir, as defined by the filesystem.

        :param path: sequence making up the path

        :todo: add relative path functionality (fix adding of leading path_separator)
        """
        if isinstance(path, basestring):
            result = path
        else:
            result = ""
            for pathelement in path:
                result += self.path_separator + pathelement

        result = result.replace('~', self.home_dir)
        result = result.replace('//', '/')
        return result
