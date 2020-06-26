'''
Author: Ashutosh Srivastava
Python3 solution
'''

import math
def sieve_of_erasthosthenes(arr,n):
    for i in range(2,int(math.sqrt(n))+1):
        if(arr[i] != False):
            for j in range(i*i,n+1,i):
                arr[j]=False
    return arr

for _ in range(int(input())):
    data=int(input())
    list_=[True for i in range(data+1)]
    arr=sieve_of_erasthosthenes(list_,data)
    arr[1]=False
    for i in range(0,data):
        if(arr[i] and arr[data-i]):
            print(i,data-i)
            break
