# Import module with functions of interest
import bayesian_functions_hw5 as bf

# define N and theta
N = 10000
theta = 0.1

# generate file 'data5.out'
bf.make_data_flips(N,theta)

# make vector of numbers
nums = [10,100,1000]

for ind in nums:
    bf.makekposterior('data5.out',ind)
    bf.plotkposterior('kpost.out',ind)

import seaborn as sns
import numpy as np
from decimal import *
import matplotlib.pyplot as plt
num_read = 10000

bf.makekposterior('data5.out',num_read)

theta,posterior = np.loadtxt('kpost.out', delimiter=",", unpack=False,dtype="|S100")
theta = [Decimal(x.decode('UTF-8')) for x in theta]
#posterior = [(Decimal(x.decode('UTF-8'))) for x in posterior]
posterior = [Decimal.ln(Decimal(x.decode('UTF-8'))) for x in posterior]
plt.figure()
plt.plot(theta,posterior)
plt.xlabel('Theta')
plt.ylabel('Log Posterior probability')
plt.title('Log Posterior probability for coin flip for M = {} points'.format(num_read))
plt.savefig('posterior_M_{}'.format(num_read))
