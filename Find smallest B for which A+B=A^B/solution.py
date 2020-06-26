# This was my solution submitted and passed all the test cases
'''
Author: Ashutosh Srivastava
Python3 solution
'''
		
def solution(data, n):
    for i in data:
        num=data.count(i)
        if(num>n):
            data=list(filter(lambda x: x != i, data))
    return(data)

import math
A=int(input())
copy=A #to create a copy of input
count=-1
flag=0
while(A!=0):
    if(A%2==0): #to count the first occurence of zero from right in binary
        count+=1
        flag=1
        break
    A=A//2
    count+=1
if(flag==1):
    print("B=",int(math.pow(2,count)))
else:
    print("B=",copy+1)
