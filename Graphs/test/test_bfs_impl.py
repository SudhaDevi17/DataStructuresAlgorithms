import unittest
from scripts.implement_bfs import Node

class TestProgram(unittest.TestCase):

    def create_graph(self):
        graph = Node('A')
        graph.addchild('B').addchild("C").addchild("D")
        graph.children[0].addchild('E').addchild('F')
        graph.children[0].children[1].addchild('I').addchild('J')
        graph.children[2].addchild('G').addchild('H')
        graph.children[2].children[0].addchild('K')
        self.assertEqual(graph.bfs([]) , ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])


