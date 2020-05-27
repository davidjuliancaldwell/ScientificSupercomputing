#!/usr/bin/python
# make node Class
# maked linkedlist class
# make stack class!

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
            
    # below are for my own edification
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.nextNode
        return count
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else: 
                current = current.nextNode
        
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else: 
                previous = current
                current = current.nextNode
            
        if previous == None:
            self.head = current.nextNode
        elif (current == self.tail):
            self.tail = previous
            self.tail.nextNode = None
        else: 
            previous.nextNode = current.nextNode
                
class Stack:
    def __init__(self):
        self.head = None
        self.N = 0
    
    def push(self,i):
        n = Node(i)
        n.data = i
        n.nextNode = self.head
        self.head = n
        self.N = self.N + 1 

    def pop(self):
        if self.head == None:
            raise Exception("Error: Empty Stack")
        else:  
            i = self.head.data
            self.head = self.head.nextNode
            self.N = self.N - 1
            return i
        
    def top(self):
        if self.head == None:
            raise Exception ("Error: Empty Stack")
        else:  
            i = self.head.data
            return i  
    
    def size(self):
        return self.N
         
    def isEmpty(self):
        if (self.N == 0):
            return True
        else:
            return False 
            
            