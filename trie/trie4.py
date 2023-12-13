#prefixtrie
class Trienode:
    def __init__(self):
        self.child={}
        self.is_end=False
class Prefixtrie:
    def __init__(self):
        self.root=Trienode()
    def insert(self,word):
        for i in range(1,len(word)+1):
            prefix=word[:i]
            self.prefixinsert(prefix)
    def prefixinsert(self,prefix):
        node=self.root
        for char in prefix:
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
t=Prefixtrie()
t.insert("anu")
t.insert("aju")
print(t.search("aju"))

        
        