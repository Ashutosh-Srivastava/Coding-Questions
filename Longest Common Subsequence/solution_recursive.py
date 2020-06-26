'''
Author: Ashutosh Srivastava
Python3 solution
'''

def lcs(p,q,n,m):
    if(n==0 or m==0):
        return 0
    elif(p[n-1]==q[m-1]):
        return 1+lcs(p,q,n-1,m-1)
    else:
        return max(lcs(p,q,n-1,m),lcs(p,q,n,m-1))    
a=input()
b=input()
print(lcs(a,b,len(a),len(b)))
