# -*- coding: utf-8 -*-

import unittest
import exceptions
import operator

from ledger import *
# Fallback to python 2 naming
try:
    from io import *
except ImportError:
    from StringIO import *
from datetime import *

class JournalTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_(self):
        pass
 
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(JournalTestCase)

if __name__ == '__main__':
    unittest.main()
