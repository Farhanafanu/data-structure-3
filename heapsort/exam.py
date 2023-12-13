def heapfy(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapfy(arr,n,i)
def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapfy(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapfy(arr,i,0)
    return arr
arr=[8,3,6,10,32]
s=heapsort(arr)
print(s)