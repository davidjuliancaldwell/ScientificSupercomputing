import numpy as np
import random as random
import math
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def generate_flips(N,theta):

    gen_values = np.array([random.random() for i in range(N)])
    output = (gen_values < theta)*1

    return output

def make_data_flips(N,theta):

    samps = list((generate_flips(N,theta)))
    output = ( ", ".join( str(e) for e in samps ) )
    f = open('data.out', 'w')
    f.write(output)

def prior(theta,a,b):
    # beta prior
    coeff = 1/((math.gamma(a)*math.gamma(b))/(math.gamma(a+b)))
    p_theta = coeff*(theta**(a-1)*(1-theta)**(b-1))

    return p_theta

def likelihood(y,theta):
    z = sum(y)
    N = len(y)
    likel = (theta**z)*(1-theta)**(N-z)

    return likel

def kposterior(theta,y):

    likel = likelihood(y,theta)
    prior_val = prior(theta,1,1)

    posterior = likel*prior_val
    return posterior

def makekposterior(file):
    y = np.loadtxt(file, comments="#", delimiter=",", unpack=False)
    theta = np.linspace(0,1,100)
    posterior = likelihood(y,theta)*prior(theta,1,1)
    f_out = open('kpost.out', 'w')
    theta_out = ( ", ".join( str(e) for e in theta ) )
    posterior_out = ( ", ".join( str(e) for e in posterior ) )
    f_out.write(theta_out)
    f_out.write('\n')
    f_out.write(posterior_out)

def plotkposterior(file):
    theta,posterior = np.loadtxt(file, delimiter=",", unpack=False)
    plt.figure()
    plt.plot(theta,posterior)
    plt.xlabel('Theta')
    plt.ylabel('Posterior probability')
    plt.title('Posterior probability for coin flip')
    plt.savefig('posterior_theta_figure.png')
