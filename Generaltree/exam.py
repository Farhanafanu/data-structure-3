class Gtree:
    def __init__(self,key) -> None:
        self.key=key
        self.child=[]
    def insert(self,data):
        newchild=Gtree(data)
        self.child.append(newchild)
    def search(self,data):
        if self.key is None:
            return None
        elif self.key==data:
            return True
        else:
            for child in self.child:
                if child.search(data):
                    return True
            return False
    def delete(self,data):
        if self.key is None:
            return None
        elif self.key==data:
            if self.child:
                newroot=self.child[0]
                self.key=newroot.key
                oldchild=self.child
                self.child=newroot.child
                for oldchild in oldchild[1:]:
                    self.insert(oldchild.key)
        else:
            for child in self.child:
                if child.key==data:
                    self.child.remove(child)
                    child.delete(data)
    def printtree(self):
        print(self.key)
        for child in self.child:
            child.printtree()
t=Gtree(10)
t.insert(9)
t.insert(12)
t.delete(10)
t.printtree()
s=t.search(9)
print(s)
        