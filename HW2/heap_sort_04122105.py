class Solution(object): 
    def heapify(self,array,n,i):
        c1 = 2*i+1
        c2 = 2*i+2
        Biggest = i
        if i >= n:
            return
        if c1 < n and array[i] < array[c1]:
            Biggest = c1
        if c2 < n and array[Biggest] < array[c2]:
            Biggest = c2
        if Biggest != i:
            array[i],array[Biggest] = array[Biggest],array[i]
            heapify(array,n,Biggest)

    def buildheap(self,array,n):
        lastnode = n-1
        parent = (lastnode-1)//2
        while parent >= 0:
            heapify(array,n,parent)
            parent = parent - 1

 
    def heap_sort(self,array):
        buildheap(array,len(array))
        i = len(array)-1
        a = []
        while i >= 0:
            a.insert(0,array[0]) 
            array[i],array[0] = array[0],array[i]
            heapify(array,i,0)
            i = i - 1
        print(a)
