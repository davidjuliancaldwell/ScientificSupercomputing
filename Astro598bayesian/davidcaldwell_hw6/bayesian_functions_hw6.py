import numpy as np
import random as random
import math
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def makeuniform_x(N):
    x_vec = np.array([random.random() for i in range(N)])
    x_2 = x_vec**2
    plt.figure()
    plt.hist(x_2,bins=100)
    plt.xlabel('x**2')
    plt.ylabel('Count')
    plt.title('Histogram of x**2 for N = {}'.format(N))
    plt.savefig('hist_x_2_N_{}'.format(N))

def makeuniform_theta(N):
    theta_vec = np.array([random.uniform(0,2*np.pi) for i in range(N)])
    m = np.tan(theta_vec)
    plt.figure()
    plt.hist(m,bins=100,range=[-10,10])
    plt.xlabel('slope m')
    plt.ylabel('Count')
    plt.title('Histogram of m for N = {}'.format(N))
    plt.savefig('hist_m_N_{}'.format(N))

def makeuniform_jeffreys(N,sig_min,sig_max):
    log_s = np.array([np.log(random.uniform(sig_min,sig_max)) for i in range(N)])
    plt.figure()
    plt.hist(log_s,bins=100)
    plt.xlabel('log sigma')
    plt.ylabel('Count')
    plt.title('Histogram of log sigma for N = {}'.format(N))
    plt.savefig('hist_log_sigma_N_{}'.format(N))
