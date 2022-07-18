import unittest

class TestAnagrams(unittest.TestCase):

    def test_groupAnagrams(self):
        import sys
        sys.path.insert(0 , '../scripts')
        from GroupAnagrams import groupAnagrams
        test_string = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected_string = [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
        result = groupAnagrams(test_string)

        self.assertEqual(expected_string , result)

    def test_optimizedGroupAnagrams(self):
        import sys
        sys.path.insert(0, '../scripts')
        from GroupAnagrams import optimizedGroupAnagrams

        test_string = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected_string = [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
        result = optimizedGroupAnagrams(test_string)
