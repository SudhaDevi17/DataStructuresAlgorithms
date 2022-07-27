class Node:

    def __init__(self, name ):
        self.children = []
        self.name = name

    def addchild(self, name ):
        self.children.append(Node(name))
        return self

    # an empty array to store and return graph nodes name
    def dfs(self, array):
        array.append(self.name)

        for child in self.children:
            print(child)
            child.dfs(array)

        return array


graph = Node('A')
graph.addchild('B').addchild('C').addchild('D')
graph.children[0].addchild('E').addchild('F')
graph.children[0].children[1].addchild('I').addchild('J')
graph.children[2].addchild('G').addchild('H')
print(graph.dfs([]))
