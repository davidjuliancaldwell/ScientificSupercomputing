import numpy as np
import math
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def findMAPestimate(file):
    theta,posterior = np.loadtxt(file, delimiter=",", unpack=False)
    ind_i = np.argmax(posterior)
    theta_max = theta[ind_i]
    print('When kposter(theta,y) is a maximum, theta = {}'.format(theta_max))
    return theta_max


def findCredibleInterval(file):
    theta,posterior = np.loadtxt(file, delimiter=",", unpack=False)
    total_a = np.trapz(posterior,x=theta)

    # build up trapz in theta
    integrals = np.array([np.trapz(posterior[0:i]/total_a,x=theta[0:i]) for i in range(len(posterior))])

    # find closest value for 2.5%
    integrals_theta_1 = abs(integrals - (2.5/100))
    theta_1 = theta[np.argmin(integrals_theta_1)]

    # find closest value for 97.5%
    integrals_theta_2 = abs(integrals - (97.5/100))
    theta_2 = theta[np.argmin(integrals_theta_2)]

    print('Theta 1 = {}, Theta 2 = {}'.format(theta_1,theta_2))

def findMeanEstimate(file):
    theta,posterior = np.loadtxt(file, delimiter=",", unpack=False)

    mean_theta = np.mean(theta)
    std_theta = np.std(theta)
    print('The mean of theta is {}, the standard deviation of theta is {}'.format(mean_theta,std_theta))
