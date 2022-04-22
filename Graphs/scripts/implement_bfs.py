class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    def addchild(self, name):
        self.children.append(Node(name))
        return self

    #Hint ! : Iterate on non empty queue to maintain the breadth-wise traversal
    def bfs(self, array):
        queue = [self] #assigned node A, start node
        #print(queue.pop(0).name)
        while len(queue)>0:
            curr = queue.pop(0)
            array.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return array

graph = Node('A')
graph.addchild('B').addchild("C").addchild("D")
graph.children[0].addchild('E').addchild('F')
graph.children[0].children[1].addchild('I').addchild('J')
graph.children[2].addchild('G').addchild('H')
graph.children[2].children[0].addchild('K')
print(graph.bfs([]))