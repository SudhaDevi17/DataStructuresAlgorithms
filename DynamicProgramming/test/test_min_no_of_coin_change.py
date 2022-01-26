# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import sys
sys.path.insert(1, '../scripts/min_no_of_coin_change')

import minNumberOfCoinsForChange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 5, 10]), 3)
