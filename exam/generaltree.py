class Gtree:
    def __init__(self,key) -> None:
        self.key=key
        self.child=[]
    def insert(self,data):
        newchild=Gtree(data)
        self.child.append(newchild)
    def delete(self,data):
        if self.key is None:
            return None
        elif self.key==data:
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
    def prtree(self):
        print(self.key)
        for child in self.child:
            child.prtree()
t=Gtree(10)
t.insert(7)
t.insert(3)
t.insert(12)
s=t.search(7)
print(s)
t.delete(10)
t.prtree()
        