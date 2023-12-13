class Trienode:
    def __init__(self) -> None:
        self.child=[]
        self.is_end=False
class Trie:
    def __init__(self) -> None:
        self.root=Trienode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.child:
                node.child[char]=Trienode()
            node=node.child[char]
        node.is_end=True
    def search(self,word):
        node=self.root
        for char in word:
            if node.child[char] is None:
                return False
            node=node.child[char]
        return node.is_end
t=Trie()
t.insert("apple")
t.insert("orenge")
print(t.search("orenge"))
        