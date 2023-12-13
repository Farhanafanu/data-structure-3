class Trienode:
    def __init__(self) -> None:
        self.child={}
        self.is_end=False
class Suffixtrie:
    def __init__(self) -> None:
        self.root=Trienode()
    def insert(self,word):
        for i in range(len(word)):
            suffix=word[i:]
            self.sufixinsert(suffix)
    def sufixinsert(self,suffix):
        node=self.root
        for char in suffix:
            if char not in node.child:
                node.child[char]=Trienode()
            node=node.child[char]
        node.is_end=True
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.child:
                return False
            node=node.child[char]
        return node.is_end
t=Suffixtrie()
t.insert("banana")
print(t.search("ba"))
