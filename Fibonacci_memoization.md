'''
Author: Ashutosh Srivastava
Python3 solution
'''

import sys
sys.setrecursionlimit(100000)

c=[0]
dict={}
def Fibo(N):
    if(N in dict):
        return dict[N]
    else:
        if(N<0):
            print("Incorrect Input")
        elif(N==0):
            return 0
        elif(N==1):
            return 1
        else:
            c[0]+=2
            dict[N]=Fibo(N-1)+Fibo(N-2)
            return dict[N]

N=int(input("Enter Nth element:"))
print(Fibo(N))
print(c[0])
