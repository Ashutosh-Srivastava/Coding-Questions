'''
Author: Ashutosh Srivastava
Python3 solution
'''

import sys
sys.setrecursionlimit(2000)
class Node:
    def __init__(self, data, left, right):
        self.data = str(data)+' '
        self.left = None
        self.right = None

def inorderTraversal(root):
    if root:
        sl = inorderTraversal(root.left)
        #print("sl=",sl)
        sc = root.data
        #print("sc=",sc)
        sr = inorderTraversal(root.right)
        #print("sr=",sr)
        #print(sl+" ",sc+" ",sr)
        return sl+sc+sr
    else:
        #print("else")
        return ''

def getDepth(root, depth):
    if root:
        dl = getDepth(root.left, depth+1)
        dr = getDepth(root.right, depth+1)
        depth = max(dl,dr)
    else:
        depth -= 1
    return depth

def swap(root, depth, height):
    if root:
        if depth == height:
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            swap(root.left, depth, height+1)
            swap(root.right, depth, height+1)
        

N = int(input())
Tree = [Node(i, None, None) for i in range(1, N+1)]
root = Tree[0]
for i in range(N):
    a, b = input().split(' ')
    a, b = [int(a)-1, int(b)-1]#Convert to zero index
    Tree[i].left = Tree[a] if a > 0 else None
    Tree[i].right = Tree[b] if b > 0 else None
depth = getDepth(root,1)
print(inorderTraversal(root))
print('depth',depth)
T = int(input())
for i in range(T):
    k = int(input())
    H = [k*i for i in range(1,N) if k*i <= depth]
    print('H = ',H)
    for h in H:
        swap(root,h,1)
    print(inorderTraversal(root))
    #print('depth',depth)
