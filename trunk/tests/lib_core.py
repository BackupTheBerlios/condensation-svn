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

import unittest

import lib.core


class CONObjectTest(lib.core.CONObject):

    _attribute_definitions = (
        ('string', 'string', 'string'),
        ('integer', 'integer', 0),
        ('stringlist', 'string[]', ['string1', 'string2']),
    )
    _signal_list = (())

    def __init__(self):
        lib.core.CONObject.__init__(self)


lib.core.CONObject.register_attribute_type(
    'CONObjectTest',
    CONObjectTest.object_serializer,
    CONObjectTest.object_deserializer)



class CONBorgTest(lib.core.CONBorg):

    _attribute_definitions = (
        ('string', 'string', 'string'),
        ('stringlist', 'string[]', ['string1', 'string2']),
    )
    _signal_list = (())

    def __init__(self):
        lib.core.CONBorg.__init__(self)




class CONBorgTest2(lib.core.CONBorg):

    _attribute_definitions = (
        ('string', 'string', 'string'),
        ('stringlist', 'string[]', ['string1', 'string2']),
    )
    _signal_list = (())

    def __init__(self):
        lib.core.CONBorg.__init__(self)





class CONObjectCollectionTest(lib.core.CONObject):

    _attribute_definitions = (
        ('string', 'string[]', []),
        ('integer', 'integer[]', []),
        ('daobjtest', 'CONObjectTest[string, integer]', [])
    )
    _signal_list = (())

    def __init__(self):
        lib.core.CONObject.__init__(self)


lib.core.CONObject.register_attribute_type(
    'CONObjectCollectionTest',
    CONObjectCollectionTest.object_serializer,
    CONObjectCollectionTest.object_deserializer)



class TestCore(unittest.TestCase):

    def test_CONObject_attribute_initialization(self):
        """
        Test the initialization of attributes.
        """
        testobj = CONObjectTest()
        self.run_attribute_initialization_test(testobj)


    def test_CONBorg_attribute_initialization(self):
        """
        Test the initialization of attributes.
        """
        testobj = CONBorgTest()
        self.run_attribute_initialization_test(testobj)


    def run_attribute_initialization_test(self, testobj):
        self.assertEqual(testobj.string, 'string')
        self.assertEqual(list(testobj.stringlist), ['string1', 'string2'])




    def test_CONObject_attribute_persistence(self):
        """
        Test the persistence of attributes.
        """
        testobj = CONObjectTest()
        self.run_persistence_test(testobj)


    def test_CONBorg_attribute_persistence(self):
        """
        Test the persistence of attributes.
        """
        testobj = CONBorgTest()
        self.run_persistence_test(testobj)


    def run_persistence_test(self, testobj):
        # test setting and reading an string attribute
        testobj.string = 'something'
        self.assertEqual(testobj.string, 'something')

        # test setting and reading an string list attribute
        stringlist = ['something', 'something else']
        testobj.stringlist = stringlist
        self.assertEqual(testobj.stringlist, stringlist)




    def test_CONObject_inter_object(self):
        """
        Test the locality of attributes. (In lib.core.CONObject the attributes are local to each object)
        """
        obj1 = CONObjectTest()
        obj2 = CONObjectTest()

        obj1.string = 'inter_test'
        self.assertNotEqual(obj1.string, obj2.string)




    def test_CONBorg_inter_object(self):
        """
        Test the locality of attributes. (In lib.core.CONBorg the attributes are local to the class)
        """
        obj1 = CONBorgTest()
        obj2 = CONBorgTest()

        obj1.string = 'inter_test'
        self.assertEqual(obj1.string, obj2.string)



    def test_CONBorg_inter_class(self):
        """
        Test the locality of attributes. (In lib.core.CONBorg the attributes are local to the class)
        """
        obj1 = CONBorgTest()
        obj2 = CONBorgTest2()

        obj1.string = 'inter_test'
        self.assertNotEqual(obj1.string, obj2.string)



    def dtest_type_checking(self):
        testobj = CONObjectTest()

        # test string type checking
        self.assertRaises(Exception, self.set_string_to_int, testobj)



    def test_CONObject_collection_indexing(self):
        testobj = CONObjectCollectionTest()

        for x in xrange(20):
            obj = CONObjectTest()
            obj.string = lib.core.Util.random_string(10)
            obj.integer = lib.core.Util.random_integer(0, 100000)
            testobj.daobjtest.add(obj)

        print testobj.daobjtest
















    def set_string_to_int(self, testobj):
        testobj.string = 10


