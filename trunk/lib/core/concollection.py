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

from signalsource import SignalSource

class CONCollection(SignalSource):

    def __init__(self, basetype=None):
        self._elements = []
        self._indices = {}
        self._unique_indices = {}
        self._basetype = basetype



    def __iter__(self):
        self._iter = self._elements.__iter__()
        return self



    def next(self):
        return self._iter.next()



    def __len__(self):
        return len(self._elements)



    def __contains__(self, item):
        return item in self._elements


    def __copy__(self):
        result = DACollection(self._basetype)
        result._elements = self._elements.copy()
        result._indices = self._indices.copy()
        result._unique_indices = self._unique_indices.copy()
        return result


    def __getitem__(self, index):
        return self._elements[index]



    def __setitem__(self, index, value):
        # TODO: remove old element from indices
        # TODO: add new element to indices
        self._elements[index] = value



    def __repr__(self):
        return str(self._elements)



    def add(self, element):
        for name, index in self._unique_indices.iteritems():
            if getattr(element, name) in index:
                raise Exception('Two objects with the same unique index.')

        elem_index = len(self._elements)
        self._elements[elem_index:] = [element]

        for name, index in self._indices.iteritems():
            value = getattr(element, name)
            if value not in self._indices[name]:
                self._indices[name][value] = []
            self._indices[name][value].append(elem_index)

        for name, index in self._unique_indices.iteritems():
            value = getattr(element, name)
            # no need to check for uniqeness, done already
            self._unique_indices[name][value] = elem_index



    def add_unique_index(self, name):
        index = {}
        self._unique_indices[name] = index

        if len(self._elements) > 0:
            for i, elem in enumerate(self._elements):
                value = getattr(elem, name)
                if value in index:
                    raise Exception('Two objects with the same unique index.')
                index[value] = i



    def add_index(self, name):
        index = {}
        self._indices[name] = index

        if len(self._elements) > 0:
            for i, elem in enumerate(self._elements):
                value = getattr(elem, name)
                if value not in index:
                    index[value] = []
                index[value].append(i)



    def get_element(self, index, value):
        if index not in self._unique_indices:
            raise Exception('no such index')
        if value not in self._unique_indices[index]:
            raise Exception('no element with this value')
        return self._elements[self._unique_indices[index][value]]



    def get_elements(self, index, value):
        if index not in self._indices:
            raise Exception('no such unique index')
        if value not in self._indices[index]:
            raise Exception('no element with this value')
        retlist = []
        for i in self._indices[index][value]:
            retlist.append(self._elements[i])
        return retlist
