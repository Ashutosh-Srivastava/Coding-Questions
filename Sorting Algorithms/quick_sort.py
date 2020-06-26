'''
Author: Ashutosh Srivastava
Python3 solution
'''

def partition(A,p,r):
    i=p-1
    pivot=A[r]
    for j in range(p,r):
        if(A[j]>pivot):   #if(A[j]<pivot): <-- ascending order
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def Quick(A,p,r):
    if(p<r):
        set=partition(A,p,r)
        Quick(A,p,set-1)
        Quick(A,set+1,r)
    
data=[10,5,7,8,6]
Quick(data,0,len(data)-1)
print(data)
