#!/usr/bin/python 

import Node

class BinarySearchTree:
    def __init__(self):
        self.N = 0
        self.root = None
        
    def insert(self,i):
        n = Node.Node()
        n.data = i
        self.N = self.N+1
        
        if (self.root==None):
            self.root = n
        else:
            root = self.root
            self.insertInner(root,n)
            
    def insertInner(self,local_root,n):
        # local_root = root
        
        # check to make sure not Null to start
        if local_root == None:
            raise Exception ("Local Root is Null!")
        
        # go left
        if (n.data < local_root.data):
            if (local_root.left == None):
                local_root.left = n
            else:
                self.insertInner(local_root.left,n)
        else:
            if(local_root.right == None):
               local_root.right = n 
            else:
               self.insertInner(local_root.right,n)
              
    def find(self,i):
        root = self.root
        return self.findInner(root,i)
    
    def findInner(self,local_root, i):
        if (local_root == None):
            return False
        elif (local_root.data ==i):
            return True
        elif (i <local_root.data):
            return self.findInner(local_root.left,i)
        else:
            return self.find(local_root.right,i)
    
    def traverse(self):
        self.traverseInner(self.root)
    
    def traverseInner(self,local_root):
        if (local_root == None):
            return
        else:
            self.traverseInner(local_root.left)
            print(local_root.data)
            self.traverseInner(local_root.right)
            
    def minBST(self):
        if (self.root == None):
            raise Exception("Root is null!")
        
        local_root = self.root
        i = local_root.data

        while (local_root != None):  
            i = local_root.data
            local_root  = local_root.left
        
        return i
    
    def maxBST(self):
        if (self.root == None):
            raise Exception("Root is null!")
            
        local_root = self.root
        i = local_root.data
        
        while (local_root != None):
            i= local_root.data
            local_root = local_root.right
        
        return i
    
    def size(self):
        return self.N
    
    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False 
            
             