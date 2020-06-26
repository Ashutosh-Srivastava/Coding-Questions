'''
Author: Ashutosh Srivastava
Python3 solution
'''

def lcs(x,y):
    n=len(x)
    m=len(y)
    table=[[None]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                table[i][j]=0
            elif(x[i-1] == y[j-1]):
                table[i][j]=table[i-1][j-1]+1
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table    #return table[n][m]<- direct value

def print_subset_all(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in print_subset_all(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R.update(print_subset_all(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(print_subset_all(C, X, Y, i-1, j))
        return R

x=input()
y=input()
lcs_table=lcs(x,y)
'''for i in range(0,len(x)+1):
    for j in range(0,len(y)+1):
        print(lcs_table[i][j],end=" ")
    print()'''
print(lcs_table[len(x)][len(y)])
comb=print_subset_all(lcs_table,x,y,len(x),len(y))
#print(comb)
comb=sorted(comb)
print(comb[0])
