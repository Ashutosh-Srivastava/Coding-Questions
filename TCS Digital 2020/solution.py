'''
Author: Ashutosh Srivastava
Python3 solution
'''

import math
dict_main={}
def cal(N):
    if N in dict_main:
        return dict_main[N]
    elif N not in dict_main:
        if(N%2==0):
            dict_main[N]=0
            return 0
        else:   
            flag=0
            for i in range(3,int(math.sqrt(N))+1,2):
                if(N%i==0):
                    flag=1
                    break
            if(flag==0):
                dict_main[N]=1
                return 1
            else:
                dict_main[N]=0
                return 0

def sexy_pairs(A,B):
    res=0
    for i in range(A,B-5,2):
        if(cal(i) and cal(i+6)):
            res+=1
    return res

A,B=map(int,input().split())
if(A%2==0):
    print(sexy_pairs(A+1,B))
else:
    print(sexy_pairs(A,B))
