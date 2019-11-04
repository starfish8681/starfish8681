class Solution(object): 
    def Merge(self,A,B):
        C = []
        i = 0 ; j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i = i+1
            elif A[i] >= B[j]:
                C.append(B[j])
                j = j+1
        if i == len(A):    
            C = C+B[j:]
        elif j == len(B):   
            C = C+A[i:]
        return C


    def merge_sort(self,c):
        n = len(c)
        if n < 2:
            return c
        else:
            middle = n//2
            A = c[:middle]
            B = c[middle:]
        
            A = self.merge_sort(A)
            B = self.merge_sort(B)
            C = self.Merge(A,B)
            return C
