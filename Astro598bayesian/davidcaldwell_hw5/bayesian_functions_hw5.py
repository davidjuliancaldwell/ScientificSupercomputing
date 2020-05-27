import numpy as np
import random as random
import math
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from decimal import *


#getcontext().traps = []
#getcontext().flags = []

setcontext(ExtendedContext)
#getcontext().prec = 100000
getcontext().Emin = -999999999999999999

def generate_flips(N,theta):

    gen_values = np.array([random.random() for i in range(N)])
    output = (gen_values < theta)*1

    return output

def make_data_flips(N,theta):

    samps = list((generate_flips(N,theta)))
    output = ( ", ".join( str(e) for e in samps ) )
    f = open('data5.out', 'w')
    f.write(output)

def prior(theta):

    if (0.45<=theta and theta<=0.55):
        p_theta = 9.1
    elif (theta<0.45 or (0.55<theta and theta<=1)):
        p_theta = 0.1
    else:
        p_theta = 0

    return p_theta

def likelihood(y,theta):
    z = Decimal(sum(y))
    N = Decimal(len(y))
    theta_dec = Decimal(theta)
    likel = Decimal((theta_dec**z)*(Decimal(1)-theta_dec)**Decimal((N-z)))
    #likel = (z*np.log(theta)) + ((N-z)*np.log(1-theta))
    #likel = np.exp(likel)
    return likel

def kposterior(theta,y):

    likel = likelihood(y,theta)
    prior_val = prior(theta)

    posterior = likel*prior_val
    return posterior

def makekposterior(file,num_read):
    y_total = np.loadtxt(file, comments="#", delimiter=",", unpack=False)
    y = y_total[0:num_read]
    #theta = np.linspace(0,1,100000000)
    theta = np.linspace(0,1,1000)
    prior_total = np.array([Decimal(prior(x)) for x in theta])
    posterior_total = np.array([likelihood(y,x) for x in theta])
    posterior = posterior_total*prior_total
    #posterior = likelihood(y,theta)*prior_total
    f_out = open('kpost.out', 'w')
    theta_out = ( ", ".join( str(e) for e in theta ) )
    posterior_out = ( ", ".join( str(e) for e in posterior ) )
    f_out.write(theta_out)
    f_out.write('\n')
    f_out.write(posterior_out)

def plotkposterior(file,num_read):
    theta,posterior = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    theta = [Decimal(x.decode('UTF-8')) for x in theta]
    posterior = [Decimal(x.decode('UTF-8')) for x in posterior] 
    plt.figure()
    plt.plot(theta,posterior)
    ymax = np.max(posterior)     
    #axes = plt.gca()
    #axes.set_ylim([0,ymax])
    plt.xlabel('Theta')
    plt.ylabel('Posterior probability')
    plt.title('Posterior probability for coin flip for M = {} points'.format(num_read))
    plt.savefig('posterior_M_{}.png'.format(num_read))
