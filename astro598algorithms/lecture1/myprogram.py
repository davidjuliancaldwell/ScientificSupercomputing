# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 11:16:09 2016

@author: David

astro598algorithms lecture, file myprogram.py
"""

import mymath

a = mymath.Complex(1.0,2.0)
b = mymath.Complex(3.0,4.0)

c = mymath.Complex.add(a,b)

print c.real
print c.imag