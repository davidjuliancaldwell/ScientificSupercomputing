#!/usr/bin/python

class Node:
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_head(self,i):
        n = Node()
        n.data = i
        n.nextNode = None
        
        if(self.head==None):
            self.head = n
            self.tail = n
        else:
            n.nextNode = self.head
            self.head = n
        
    def delete_at_head(self):
        x = self.head.data
        self.head = self.head.nextNode
        if(self.head==None):
            self.tail = None
        return x
        
    def insert_at_tail(self,i):
        n = Node()
        n.data = i
        n.next = None
        if (self.head==None):
            self.head = n
            self.tail = n
        elif (self.head == self.tail):
            self.head.next = n
            self.tail = n
        else:
            self.tail.nextNode = n
            self.tail = n

class Queue:
    def __init__(self):
        self.head = None
        self.tail= None
        self.N = 0
    
    def put(self,i):
        Nnew = Node()
        Nnew.data = i
        
        # null list
        
        if (self.head == None):
            self.head = Nnew
            self.tail = Nnew
        
        # one node
        elif (self.head==self.tail):
            self.head.nextNode = Nnew
            self.tail = Nnew
        
        # all other cases
        else:
            self.tail.nextNode = Nnew
            self.tail = Nnew
        
        self.N = self.N + 1
        
    def get(self):
        if(self.head == None):
            raise Exception("Error: Empty Stack")
        i = self.head.data
        self.head = self.head.nextNode
        self.N = self.N - 1
        if self.N == 0:
            self.head = None
            self.tail = None
        return i
    
    def front(self):
        if(self.head == None):
            raise Exception("Error: Empty Stack")
        i = self.head.data
        return i
            
    def size(self):
        sizeQ = self.N
        return sizeQ
        
    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False
