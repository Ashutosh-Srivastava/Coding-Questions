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
