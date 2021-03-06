#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 11:18:52 2016

@author: David

homework 1
"""

g = 9.81

class Position:
    
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
class Velocity:
    
    def __init__(self,vx=0.0,vy=0.0,vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
class Particle(Position,Velocity):
    
    def __init__(self,m,x,y,z,vx,vy,vz):
        self.mass = m
        Position.__init__(self,x,y,z)
        Velocity.__init__(self,vx,vy,vz)
        
    @staticmethod
    def force(p1,p2):
        distance = ((p1.x-p2.x)**2.0+(p1.y-p2.y)**2.0+(p1.z-p2.z)**2.0)**(0.5)
        f = g*p1.mass*p2.mass/(distance**2)
        return f
        
        
