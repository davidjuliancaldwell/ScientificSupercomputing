import bayesian_functions_hw7 as bf

# part a and b- generate data points
bf.makedata(1000,2,1)

# part d - run mcmc

# initialize parameters
N = [10000,100000,1000000]
mu_min = -10
mu_max = 10
sig_min = 0.1
sig_max = 10
delta = 0.1

#for n in N:
#    bf.mcmc(n,mu_min,mu_max,sig_min,sig_max,delta,'data.out')

# part e
for n in N:
    bf.heatmap('mcmc_N_{}.out'.format(n))

# part f
for n in N:
    bf.findMAP('mcmc_N_{}.out'.format(n))

# part g
for n in N:
    bf.findMean('mcmc_N_{}.out'.format(n))

# part h
for n in N:
    bf.makeHistMu('mcmc_N_{}.out'.format(n))

# part i
for n in N:
    bf.findCredibleInterval('mcmc_N_{}.out'.format(n))
