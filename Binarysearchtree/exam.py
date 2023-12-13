class BST:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None
    def insert(self,data):
        if self.key is None:
            self.key=data
        elif self.key==data:
            return
        else:
            if self.key>data:
                if self.left:
                    self.left.insert(data)
                else:
                    newchild=BST(data)
                    self.left=newchild
            elif self.key<data:
                if self.right:
                    self.right.insert(data)
                else:
                    newchild=BST(data)
                    self.right=newchild
    def search(self,data):
        if self.key is None:
            return None
        elif self.key==data:
            return True
        else:
            if self.key>data:
                if self.left is None:
                    return False
                else:
                    return self.left.search(data)
            elif self.key<data:
                if self.right is None:
                    return False
                else:
                    return self.right.search(data)
    def delete(self,data):
        if self.key is None:
            return None
        elif self.key>data:
            if self.left:
                self.left=self.left.delete(data)
        elif self.key<data:
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
            else:
                minroot=self.right.findmin()
                self.key=minroot.key
                self.right=self.right.delete(minroot.key)
        return self
    def findmin(self):
        current=self
        while current.left is not None:
            current=current.left
        return current
    def maxval(self,node):
        if node is None:
            return 1
        else:
            leftmax=self.maxval(node.left)
            rightmax=self.maxval(node.right)
            value=max(leftmax,rightmax,node.key)
            return value
    def minval(self,node):
        if node is None:
            return 1
        else:
            leftmin=self.minval(node.left)
            rightmin=self.minval(node.right)
            value=min(leftmin,rightmin,node.key)
            return value
    def isbst(self):
        if self.key is not None:
            left=self.left is None or(self.left.key<self.key and self.left.isbst())
            right=self.right is None or (self.right.key>self.key and self.right.isbst())
            return left and right
    def closest(self,target):
        closest=self.key
        current=self
        while current:
            if abs(current.key-target)<abs(closest-target):
                closest=current.key
            if target<current.key:
                current=current.left
            elif target>current.key:
                current=current.right
            else:
                return closest
        return closest
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key)
t=BST(8)
t.insert(16)
t.insert(65)
t.insert(2)
t.insert(23)
t=t.delete(8)
b=t.isbst()
print(b)
target=9
c=t.closest(target)
print(c)
s=t.search(65)
print(s)
t.inorder()
max=t.maxval(t)
print("max",max)
min=t.minval(t)
print("min",min)

        