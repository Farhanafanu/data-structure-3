class Trienode:
    def __init__(self):
        self.child={}
        self.is_end=False
class Suffixtree:
    def __init__(self):
        self.root=Trienode()
    def insert(self,word):
        for i in range(len(word)):
            suffix=word[i:]
            self.suffixinsert(suffix)
    def suffixinsert(self,suffix):
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
        return True
t=Suffixtree()
t.insert("apple")
t.insert("orenge")
print(t.search("apples"))

        
        