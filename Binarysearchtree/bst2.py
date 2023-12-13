class BST:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def insert(self,data):
        if self.key is None:
            self.key=data
        if self.key==data:
            return
        if self.key>data:
            if self.left:
                self.left.insert(data)
            else:
                newchild=BST(data)
                self.left=newchild
        else:
            if self.right:
                self.right.insert(data)
            else:
                newchild=BST(data)
                self.right=newchild
    def search(self,data):
        if self.key is None:
            return False
        elif self.key==data:
            return True
        elif data<self.key:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
            
        elif data>self.key:
            if self.right is None:
                return False
            else:
                return self.right.search(data)
    def delete(self,data):
        if self.key is None:
            return self
        if data<self.key:
            if self.left:
                self.left=self.left.delete(data)
        elif data>self.key:
            if self.right:
                self.right=self.right.delete(data)
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            elif self.right is None:
                temp=self.left
                self=None
                return temp
            minrightnode=self.right.findmin()
            self.key=minrightnode.key
            self.right=self.right.delete(minrightnode.key)
        return self
    def findmin(self):
        current=self
        while current.left is not None:
            current=current.left
        return current
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()
    def isbst(self):
        if self.key is not None:
            left=self.left is None or (self.left.key<self.key and self.left.isbst())
            right=self.right is None or (self.right.key>self.key and self.right.isbst())
            return left and right
        else:
            return True
t=BST(10)
t.insert(9)
t.insert(7)
t=t.delete(10)
t.inorder()
s=t.isbst()
print(s)        