
class SuffixTrie:

    def __init__(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.buildTree(string)

    def buildTree(self, string):

        for i in range(len(string)):
            self.insertLetter(i , string)

    def insertLetter(self, i , string):

        node = self.root

        for j in range(i, len(string)):
            letter = string[j]
            # search wide across keys to see if a character exists
            # synonimous to node.keys() operation
            if letter not in node:
                node[letter] = {}
            # going deep in trie branch
            node = node[letter]
        node[self.endSymbol] = True

    def searchContains(self,  string):

        node = self.root

        for j in range(len(string)):
            letter = string[j]
            if letter not in node:
                return False
            node = node[letter]
            print(node)
        return self.endSymbol in node

trie = SuffixTrie('babc')
print(trie.root)
print(trie.searchContains('abc'))