# This is a function to calculate the CDF for a gaussian

import math
import scipy.integrate as integrate 
import numpy as np

def CumulativeGaussian(mu,sigma,y):
    
    gauss = lambda x: (1/(sigma*math.sqrt(math.pi*2)))*math.exp(-(x-mu)**2/(2*(sigma**2)))
    
    
    cg, err = integrate.quad(gauss,-np.inf,y)
    
    return cg