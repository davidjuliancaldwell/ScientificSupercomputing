#!/usr/bin/python 


# This is a function to computer the Poisson PDF

import math

def poissonPDF(n,lamb):
    
    pn = (lamb**n)*(math.exp(-lamb))/math.factorial(n)
    return pn