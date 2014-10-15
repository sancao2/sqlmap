#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from lib.core.datatype import AttribDict

class AboutDatatype(Koan):

    def test_AttribDict(self):
        foo = AttribDict()
        foo.bar = 1
        self.assertEqual(1, foo.bar)
        self.assertEqual(['_AttribDict__initialised', '__class__', '__cmp__', '__contains__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues'],dir(foo))
