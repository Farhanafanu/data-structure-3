class Maxheap:
    def __init__(self) -> None:
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    def lchild(self,i):
        return 2*i+1
    def rchild(self,i):
        return 2*i+2
    def insert(self,data):
        self.heap.append(data)
        self.heapfyup(len(self.heap)-1)
    def deletemax(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()  # Pop and return the only element
        else:
            max = self.heap[0]
            self.heap[0] = self.heap.pop()  # Replace the root with the last element
            self.heapfydown(0)
    def deltenode(self,data):
        if data not in self.heap:
            return None
        else:
            index=self.heap.index(data)
            self.heap[index]=float('inf')
            self.heapfydown(index)
            self.deletemax()
    def heapfyup(self,i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    def heapfydown(self,i):
        largset=i
        left=self.lchild(i)
        right=self.rchild(i)
        if left<len(self.heap) and self.heap[left]>self.heap[largset]:
            largset=left
        if right<len(self.heap) and self.heap[right]>self.heap[largset]:
            largset=right
        if largset!=i:
            self.heap[i],self.heap[largset]=self.heap[largset],self.heap[i]
            self.heapfydown(largset)
    def printheap(self):
        print(self.heap)
h=Maxheap()
h.insert(2)
h.insert(87)
h.insert(65)
h.insert(97)
h.deletemax()
h.printheap()