'''
Author: Ashutosh Srivastava
Python3 solution
'''

import math
def sieve_of_erasthosthenes(arr,n):
    for i in range(2,int(math.sqrt(n)+1)):
        if(arr[i] != False):
            for j in range(i*i,n+1,i):
                arr[j]=False
    return arr

if __name__ == "__main__":
    n=int(input("Enter range"))
    list_=[True for i in range(n+1)]
    arr=sieve_of_erasthosthenes(list_,n)
