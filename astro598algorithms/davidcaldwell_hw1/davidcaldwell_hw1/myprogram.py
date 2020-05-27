#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 14:13:50 2016

@author: David

homework 1
"""


import myparticle 
a = myparticle.Particle(10,1,2,3,100,50,60)
b = myparticle.Particle(100,20,30,40,5,3,2)

force = myparticle.Particle.force(a,b)
print ("The Force between the two particles in Newtons is {0}".format(force))
