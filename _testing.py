# -*- coding: utf-8 -*-
"""Script for running the tests.
"""
import unittest

VERBOSE = 0

suite = unittest.TestSuite()

dirnames = [
    'hps', 'polys'
]

for testnum in range(2):

    DIRNAME = dirnames[testnum]

    PATTERN = 'test_*.py'
    STARTDIR = DIRNAME + '/_tests'

    dirsuite = unittest.TestLoader().discover(STARTDIR, PATTERN)
    suite.addTests(dirsuite)

unittest.TextTestRunner(verbosity=VERBOSE).run(suite)
