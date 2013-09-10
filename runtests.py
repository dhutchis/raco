#!/usr/bin/env python

from raco.tests import DatalogTest
import raco.myrial.query_tests
import sys
import unittest

test_cases = [DatalogTest, raco.myrial.query_tests.TestQueryFunctions]
suites = [unittest.TestLoader().loadTestsFromTestCase(c) for c in test_cases]
all_tests = unittest.TestSuite(suites)

result = unittest.TextTestRunner(verbosity=2).run(all_tests)
sys.exit(not result.wasSuccessful())
