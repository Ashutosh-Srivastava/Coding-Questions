'''
Author: Ashutosh Srivastava
Python3 solution
'''

def heapify(A,n,i):
    l=2*i+1
    r=2*i+2
    largest=i
    if(l<n and A[l]>A[largest]):
        largest=l
    if(r<n and A[r]>A[largest]):
        largest=r
    if(largest != i):
        A[i],A[largest]=A[largest],A[i]
        heapify(A,n,largest)

def heap_sort(A):
    for i in range(len(A)//2,-1,-1):
        heapify(A,len(A),i)
    for i in range(len(A)-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)

data=[5,4,3,2,1,0,1]
heap_sort(data)
print(data)
