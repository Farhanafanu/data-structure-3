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
    def maxdelete(self):
        if self.heap is None:
            return None
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            max=self.heap[0]
            self.heap[0]=self.heap.pop()
            self.heapfydown(0)
    def heapfyup(self,i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    def heapfydown(self,i):
        largest=i
        left=self.lchild(i)
        right=self.rchild(i)
        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=i:
            self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
            self.heapfydown(largest)
    def heaprint(self):
        print(self.heap)
h=Maxheap()
h.insert(10)
h.insert(19)
h.insert(34)
h.insert(12)
h.maxdelete()
h.heaprint()