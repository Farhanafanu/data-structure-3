#minheap
class minheap:
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
    def mindelete(self):
        if self.heap is None:
            return None
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            min=self.heap[0]
            self.heap[0]=self.heap.pop()
            self.heapfydown(0)
    def heapfyup(self,i):
        while i>0 and self.heap[i]<self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    def heapfydown(self,i):
        smallest=i
        left=self.lchild(i)
        right=self.rchild(i)
        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=i:
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            self.heapfydown(smallest)
    def printheap(self):
        print(self.heap)
h=minheap()
h.insert(8)
h.insert(10)
h.insert(14)
h.insert(13)
h.insert(3)
h.mindelete()
h.printheap()