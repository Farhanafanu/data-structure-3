class Mxheap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    def insert(self,data):
        self.heap.append(data)
        self.heapfyup(len(self.heap)-1)
    def deletemax(self):
        if self.heap is None:
            return None
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            max=self.heap[0]
            self.heap[0]=self.heap.pop()
            self.heapfyup(0)
    def heapfyup(self,i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    
    def display(self):
        print(self.heap)
h=Mxheap()
h.insert(9)
h.insert(10)
h.insert(80)
h.deletemax()
h.display()
        