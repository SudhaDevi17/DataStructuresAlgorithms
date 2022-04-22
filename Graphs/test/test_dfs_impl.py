import unittest
from scripts.implement_dfs import Node

class TestProgram(unittest.TestCase):

    def create_graph(self):
        graph = Node('A')
        graph.addchild('B').addchild('C').addchild('D')
        graph.children[0].addchild('E').addchild('F')
        graph.children[0].children[1].addchild('I').addchild('J')
        graph.children[2].addchild('G').addchild('H')
        self.assertEqual(graph.dfs([]) , ["A", "B", "E", "F", "I", "J", "C", "D", "G", "H"])


