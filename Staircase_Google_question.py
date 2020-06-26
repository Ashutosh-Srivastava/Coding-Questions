'''
Author: Ashutosh Srivastava
Python3 solution
'''

import sys
sys.setrecursionlimit(100000)
dict_main={}

def recursive(N,m):
    if(N in dict_main):
        return dict_main[N]
    else:
        ans=0
        if(N<0):
            return 0
        elif(N==0):
            return 1
        else:
            for i in m:
                ans += recursive(N-i,m)
                dict_main[N]=ans
        return ans     

N=int(input("Enter the steps of the staircase: "))
m=int(input("Enter number of distinct steps: "))
step_size=[]
print("Enter the sizes: c")
for i in range(m):
    step_size.append(int(input()))
print(recursive(N,step_size))
