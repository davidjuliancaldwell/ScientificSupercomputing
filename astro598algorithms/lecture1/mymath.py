# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 11:13:00 2016

@author: David

astro598algorithms lecture, file mypath.py
"""

class Complex:
    
    def __init__(self, r=0.0, i=0.0):
        self.real=r
        self.imag=i
        
    @staticmethod
    def add(x,y):
        z=Complex(x.real+y.real,x.imag+y.imag)
        return z
        
        
