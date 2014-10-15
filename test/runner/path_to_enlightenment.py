#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import unittest

from koans.about_agent import AboutAgent
from koans.about_datatype import AboutDatatype
from koans.about_data import AboutData

def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutAgent))
    suite.addTests(loader.loadTestsFromTestCase(AboutDatatype))
    suite.addTests(loader.loadTestsFromTestCase(AboutData))

    return suite
