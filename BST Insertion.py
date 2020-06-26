'''
Author: Ashutosh Srivastava
Python3 solution
'''

class BST:
    class Node:
        def __init__(self,val):
            self.val=val
            self.right=None
            self.left=None
        
        def getval(self):
            return self.val
        
        def setval(self,nval):
            self.val=nval
        
        def get_lval(self):
            return self.left
        
        def set_lval(self,nlval):
            self.left=nlval
        
        def get_rval(self):
            return self.right
        
        def set_rval(self,nrval):
            self.right=nrval   
        
    def __init__(self,root=None):
        self.root=root
    
    def findroot(self,val):
        self.root=BST.insert(self.root,val)

    def insert(root,val):
        if(root==None):
            return BST.Node(val)
        
        if(val<root.getval()):
            root.set_lval(BST.insert(root.get_lval(),val))
        else:
            root.set_rval(BST.insert(root.get_rval(),val))
        
        return root

if __name__=='__main__':
    list_=list(input("Enter a list of numbers: ").split())
    tree = BST()    
    for x in list_:
        tree.findroot(int(x))
