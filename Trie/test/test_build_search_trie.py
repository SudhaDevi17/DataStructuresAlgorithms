import unittest

import sys
sys.path.insert(0,'..')
import script.build_search_trie
#import SuffixTrie

class TestTrie(unittest.TestCase):

    def test_trie(self):


        trie = script.build_search_trie.SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.searchContains("abc"))