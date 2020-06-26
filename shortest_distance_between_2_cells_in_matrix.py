class Value:
        def __init__(self,m,n,d,data):
                self.d=d
                self.r=m
                self.c=n
                self.i=data

def min_dist(mat,m,n):
        visit=[[None for _ in range(4)] for _ in range(4)]
        for i in range(len(mat)):
                for j in range(len(mat[0])):
                        if(mat[i][j]=='0'):
                                visit[i][j]=True
                        else:
                                visit[i][j]=False
        Q=[]
        mat[m][n]=Value(m,n,0,mat[m][n])
        Q.append(mat[m][n])
        visit[m][n]=True
        while(len(Q)>0):
                temp=Q[0]
                Q.pop(0)
                #print(temp.i," ",temp.d)
                
                if(temp.i=='d'):
                        return temp.d

                if(temp.r-1>=0 and visit[temp.r-1][temp.c]==False):
                        mat[temp.r-1][temp.c]=Value(temp.r-1,temp.c,temp.d+1,mat[temp.r-1][temp.c])
                        Q.append(mat[temp.r-1][temp.c])
                        visit[temp.r-1][temp.c]=True
                
                if(temp.r+1<len(mat) and visit[temp.r+1][temp.c]==False):
                        mat[temp.r+1][temp.c]=Value(temp.r+1,temp.c,temp.d+1,mat[temp.r+1][temp.c])
                        Q.append(mat[temp.r+1][temp.c])
                        visit[temp.r+1][temp.c]=True
                
                if(temp.c-1>=0 and visit[temp.r][temp.c-1]==False):
                        mat[temp.r][temp.c-1]=Value(temp.r,temp.c-1,temp.d+1,mat[temp.r][temp.c-1])
                        Q.append(mat[temp.r][temp.c-1])
                        visit[temp.r][temp.c-1]=True
                
                if(temp.c+1<len(mat[0]) and visit[temp.r][temp.c+1]==False):
                        mat[temp.r][temp.c+1]=Value(temp.r,temp.c+1,temp.d+1,mat[temp.r][temp.c+1])
                        Q.append(mat[temp.r][temp.c+1])
                        visit[temp.r][temp.c+1]=True
        return -1
                
n,m=map(int,input().split())
matrix=[]
for i in range(n):
        temp=input().split()
        matrix.append(temp)

source=''

for a in range(n):
        i=matrix[a]
        if('s' in i):
                source =str(a) + str(i.index('s'))
                break
print(min_dist(matrix,int(source[0]),int(source[1])))
