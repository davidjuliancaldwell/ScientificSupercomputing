import numpy as np
import random as random
import math
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta

def beta_func(theta,a,b):
    # beta prior
    numSteps = 1000
    theta_vector = np.linspace(0,1,numSteps)
    vector_int = [x**(a-1)*(1-x)**(b-1) for x in theta_vector]
    dx = 1/numSteps
    coeff = 1/np.trapz(vector_int,dx=dx)
    p_theta = coeff*(theta**(a-1)*(1-theta)**(b-1))

    return p_theta

def plot_beta_func(a,b):
    theta_list = np.linspace(0,1,1000)
    output = [beta_func(theta,a,b) for theta in theta_list]
    plt.figure()
    plt.plot(theta_list,output)
    plt.xlabel('Theta')
    plt.ylabel('Probability')
    plt.title('Probability for Beta Distribution for a = {}, b = {}'.format(a,b))
    plt.savefig('beta_dist_a_{}_b_{}.png'.format(a,b))
