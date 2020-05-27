#!/usr/bin/python 

# This is a function to compute the CDF for a poisson 

import math

def CumulativePoisson(lamb,m):
    arr = list(range(0,m+1))
    
    listCP = [(lamb**i)/math.factorial(i) for i in arr]
    cpn = math.exp(-lamb)*sum(listCP)
    
    return cpn
    