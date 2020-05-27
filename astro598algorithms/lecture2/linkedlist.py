# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:05:19 2016

@author: David
"""

# make node Class

class Node:
    def __init__(self,data=0,nextNode=None):
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
            self.tail.nextNode
            self.tail = n
            self.head.nextNode = n
        else:
            self.tail.nextNode = n
            self.tail = n
            
            
            
            
            