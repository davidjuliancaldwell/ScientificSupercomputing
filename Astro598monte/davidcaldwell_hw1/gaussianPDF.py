# this function computes the PDF for a gaussian 

import math


def gaussianPDF(x,mu,sigma):

    gp = (1/(sigma*math.sqrt(math.pi*2)))*math.exp(-(x-mu)**2/(2*(sigma**2)))
    
    return gp