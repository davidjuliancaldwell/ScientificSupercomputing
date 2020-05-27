# coinflip program

# this is the module that needs to be imported for the hw script to be run

# import modules that are needed
import numpy as np
import random as random
import matplotlib.pyplot as plt
import seaborn as sns

# define bernoulli function
def bernoulli(p):
    random_num = random.random()

    if random_num < p:
        flipped = 1
    else:
        flipped = 0

    return flipped

# define coinflip function
def coinflip_func(p,N,M):

    # generate the list
    flip_iters  =[[bernoulli(p) for x in range(N)] for y in range(M)]
    h = np.sum(flip_iters,1)

    mean_h = np.mean(h)
    var_h = np.var(h)

    print('The mean number of heads is {}, the variance of the number of heads is {}'.format(mean_h,var_h))
    fig = plt.figure()
    num_bins = 50
    #plt.hist(h)
    sns.distplot(h,kde=False)
    plt.xlabel('Number of heads')
    plt.ylabel('Number of occurences')
    plt.title('Histogram for coinflips - p = {}, N = {}, M = {}'.format(p,N,M))
    plt.savefig('histogram_p_{}_N_{}_M_{}.png'.format(p,N,M))

    return (mean_h,var_h)
