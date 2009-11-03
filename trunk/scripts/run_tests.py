#!/usr/bin/python

import sys
import unittest

sys.path.append('..')

import tests

core_suite = unittest.TestLoader().loadTestsFromTestCase(tests.TestCore)
packaging_suite = unittest.TestLoader().loadTestsFromTestCase(tests.TestPackaging)
progress_suite = unittest.TestLoader().loadTestsFromTestCase(tests.TestDAProgressMeter)

all_suites = unittest.TestSuite([core_suite, packaging_suite, progress_suite])
unittest.TextTestRunner(verbosity=2).run(all_suites)
