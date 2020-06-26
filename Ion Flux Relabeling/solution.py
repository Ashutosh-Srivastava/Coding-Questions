# This was my solution submitted and passed all the test cases
'''
Author: Ashutosh Srivastava
Python3 solution
'''

def solution(h, q):
    return [parent(h,x) for x in q]

def parent(h,i):
    depth = (2**h)-1
    res = -1
    if(depth<=i):
        return res
    else:
        breaker = True
        subtree = depth
        offset = 0
        while(breaker):
            if(not(subtree)):
                return res
            else:
                subtree = subtree//2
                LN = offset+subtree
                RN = LN+subtree
                ans = RN +1
                if((i==LN) or (i==RN)):
                    return ans
                if(i>LN):
                    offset=LN
