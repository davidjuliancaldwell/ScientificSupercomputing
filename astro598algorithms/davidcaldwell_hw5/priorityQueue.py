#!/usr/bin/python 

class priorityQueue:
    def __init__(self,M):
        self.N = 0
        self.MAX = M
        self.a = [0]*M
        
    def insert(self,i):
        self.N = self.N + 1

        if(self.N >= self.MAX):
            raise Exception("Would exceed size of array")
            
        self.a[self.N] = i
        k = self.N
        
        while ((k>1) and (self.a[k//2]>self.a[k])):
            temp = self.a[k//2]
            self.a[k//2] = self.a[k]
            self.a[k] = temp
            k = k//2

    def delMin(self):
        if (self.N == 0):
            raise Exception("Empty PriorityQueue!")
        minimum = self.a[1]
        self.a[1] = self.a[self.N]
        self.a[self.N] = 0
        self.N = self.N -1 
        k = 1
        while (2*k <= self.N):
            if ((2*k == self.N) or (self.a[2*k]<self.a[(2*k)+1])):
                j = 2*k
            else:
                j = (2*k)+1
            
            if(self.a[k]>self.a[j]):
                temp = self.a[k]
                self.a[k] = self.a[j]
                self.a[j] = temp
                k = j
            else:
                break                            
            
        return minimum

                
        
    def minimum(self):
        if (self.N == 0):
            raise Exception("Empty PriorityQueue!")
        minimum = self.a[1]
        return minimum 
        
    def size(self):
        return self.N
        
    def isEmpty(self):
        if self.N == 0:
            return True 
        else:
            return False 
        
    def isFull(self):
        if self.MAX == self.N:
            return True
        else:
            return False 
                
        
    
        