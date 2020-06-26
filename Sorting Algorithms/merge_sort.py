'''
Author: Ashutosh Srivastava
Python3 solution
'''

def merge_sort(A):
    if(len(A)>1):
        L=A[:len(A)//2]
        R=A[len(A)//2:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                A[k]=L[i]
                i+=1
                k+=1
            else:
                A[k]=R[j]
                j+=1
                k+=1
        while(i<len(L)):
            A[k]=L[i]
            i+=1
            k+=1
        while(j<len(R)):
            A[k]=R[j]
            j+=1
            k+=1
data=[7,6,5,4,3,2,1,0]
merge_sort(data)
print(data)
