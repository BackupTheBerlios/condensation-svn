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



class ManagerObject(object):

    def __init__(self, container_notebook):
        self._container_notebook = container_notebook
        self._container_notebook_page = self._container_notebook.append_page(self)



    def get_container_notebook(self):
        return self._container_notebook



    def get_menu_icon(self):
        """
        Return the item to be shown in the TreeView.
        """
        raise Exception("Not Implemented!")



    def get_menu_name(self):
        raise Exception("Not Implemented!")



    def selected(self):
        if self._container_notebook_page != None:
            self._container_notebook.set_current_page(self._container_notebook_page)


    def destroy(self):
        self._container_notebook.remove_page(self._container_notebook_page)




