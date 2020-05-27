import numpy as np
import random as random
import math
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
from scipy.interpolate import griddata
from decimal import *


setcontext(ExtendedContext)
getcontext().rounding = 'ROUND_UP'
getcontext().Emin = -99999999999999999
getcontext().Emax = 99
getcontext().rounding = ROUND_UP

def makedata(M,mu,sigma):
    gauss_vec = [random.gauss(mu,sigma) for i in range(M)]
    output = ( ", ".join( str(e) for e in gauss_vec ) )
    f = open('data.out', 'w')
    f.write(output)
    return gauss_vec

def prior_unif(a,b):
    probability = 1.0/(b-a)
    return probability

def likelihood(data,mu,sig):
    likelihood_vec = (scipy.stats.norm(mu, sig).pdf(data))
    likelihood_vec = [Decimal(i) for i in likelihood_vec]
    likelihood_total = (np.prod(likelihood_vec))
    return likelihood_total

def mcmc(N,mu_min,mu_max,sig_min,sig_max,delta,file):
    data = np.loadtxt(file, delimiter=",", unpack=False)

    x_out = [0]*N
    y_out = [0]*N

    x_initial = np.array([random.uniform(mu_min,mu_max), random.uniform(sig_min,sig_max)])
    x = x_initial
    # define priors
    prior_mu = prior_unif(mu_min,mu_max)
    prior_sig = prior_unif(sig_min,sig_max)
    prior_comb = Decimal(prior_mu*prior_sig) # combine priors
    y = prior_comb*likelihood(data,x_initial[0],x_initial[1])

    x_out[0] = x
    y_out[0] = y

    for i in range(1,N):
        s = [(random.uniform(-delta,delta)),(random.uniform(-delta,delta))]
        x_new = x + s

        if ((x_new[0] < mu_min) or (x_new[0] > mu_max) or (x_new[1]<sig_min) or (x_new[1]>sig_max)):
            y_new = -1000000000000000000000
        else:
            y_new = prior_comb*likelihood(data,x_new[0],x_new[1])

        if (y_new>y):
            x = x_new
            y = y_new
        else:
            r = random.random()

            if ((y_new/y) > r):
                x = x_new
                y = y_new

        x_out[i] = x
        y_out[i] = y

    x_out = np.array(x_out)
    f_out = open('mcmc_N_{}.out'.format(N), 'w')
    x_mu_write = ( ", ".join( str(e) for e in  x_out[:,0]) )
    x_sig_write = ( ", ".join( str(e) for e in  x_out[:,1]) )
    y_write = ( ", ".join( str(e) for e in y_out ) )
    f_out.write(x_mu_write)
    f_out.write('\n')
    f_out.write(x_sig_write)
    f_out.write('\n')
    f_out.write(y_write)

def heatmap(file):
    [mu,sig,posterior] = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    mu = np.array([float(x.decode('UTF-8')) for x in mu])
    sig = np.array([float(x.decode('UTF-8')) for x in sig])
    # Create heatmap
    N = len(mu)
    with sns.axes_style("white"):

        plt.figure()
        plt.xlim([1.5,2.5])
        plt.ylim([0.5,1.5])
        plt.hexbin(mu,sig,gridsize=250)
            #plt.hexbin(mu, sig, color="#4CB391", xlim=[1.5,2.5],ylim=[0.5,1.5])
        plt.title(r'Joint distribution plot for $\mu$ and $\sigma$ for N = {}'.format(N))
        plt.xlabel(r'$\mu$')
        plt.ylabel(r'$\sigma$')

        plt.savefig('heatmap_N_{}'.format(N))

        #lt.show()




def findMAP(file):
    [mu,sig,posterior] = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    mu = [float(x.decode('UTF-8')) for x in mu]
    sig = [float(x.decode('UTF-8')) for x in sig]
    posterior = [Decimal(x.decode('UTF-8')) for x in posterior]

    """
    ind_i = np.argmax(posterior)
    mu_max = mu[ind_i]
    sig_max = sig[ind_i]
    """
    N = len(mu)
    H,mu_hist,sig_hist = np.histogram2d(mu, sig, bins=1000, range=None, normed=True, weights=None)

    [mu_ind,sig_ind] = np.unravel_index(H.argmax(), H.shape)
    mu_max = mu_hist[mu_ind]
    sig_max = sig_hist[sig_ind]
    print('When posterior distribution is a maximum for N = {}, mu = {},sigma = {}'.format(N,mu_max,sig_max))
    return mu_max,sig_max


def findMean(file):
    [mu,sig,posterior] = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    mu = [float(x.decode('UTF-8')) for x in mu]
    sig = [float(x.decode('UTF-8')) for x in sig]
    posterior = [Decimal(x.decode('UTF-8')) for x in posterior]

    mean_mu = np.mean(mu)
    mean_sig = np.mean(sig)
    N = len(mu)

    print('For N = {}, The mean of mu is {}, the mean of sigma is {}'.format(N,mean_mu,mean_sig))


def makeHistMu(file):
    [mu,sig,posterior] = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    mu = [float(x.decode('UTF-8')) for x in mu]
    sig = [float(x.decode('UTF-8')) for x in sig]
    posterior = [Decimal(x.decode('UTF-8')) for x in posterior]

    numBins = 500
    plt.figure()
    plt.xlabel(r'$\mu$')
    plt.xlim([1.5,2.5])
    N = len(mu)
    plt.hist(mu,numBins)

    plt.title(r'Histogram for $\mu$ for N = {}'.format(N))
    plt.savefig('histMu_N_{}'.format(N))

    #plt.show()

def findCredibleInterval(file):
    [mu,sig,posterior] = np.loadtxt(file, delimiter=",", unpack=False,dtype="S100")
    mu = np.array([float(x.decode('UTF-8')) for x in mu])
    sig = np.array([float(x.decode('UTF-8')) for x in sig])
    posterior = np.array([float(Decimal(x.decode('UTF-8')).ln()) for x in posterior])

    numBins = 2000
    hist = np.histogram(mu,numBins)
    #plt.hist(mu,numBins)
    hist_center = (hist[1][1:] + hist[1][:-1]) / 2

    total_a = (np.trapz(hist[0],x=hist_center))

        # build up trapz in theta
    integrals = np.array([np.trapz(hist[0][0:i]/total_a,x=hist_center[0:i]) for i in range(len(hist_center))])

        # find closest value for 2.5%
    integrals_mu_1 = abs(integrals - (2.5/100))
    mu_1 = hist_center[np.argmin(integrals_mu_1)]

        # find closest value for 97.5%
    integrals_mu_2 = abs(integrals - (97.5/100))
    mu_2 = hist_center[np.argmin(integrals_mu_2)]
    N = len(mu)

    print('For N = {}, mu 1 = {}, mu 2 = {}'.format(N,mu_1,mu_2))
