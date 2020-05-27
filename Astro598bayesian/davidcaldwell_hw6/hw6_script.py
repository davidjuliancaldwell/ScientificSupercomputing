import bayesian_functions_hw6 as bf

# x**2
N = 10000
bf.makeuniform_x(N)

# tan(theta)
N = 10000
bf.makeuniform_theta(N)

# jeffrey's prior
N = 1000000
sig_min = 0.01
sig_max = 10000
bf.makeuniform_jeffreys(N,sig_min,sig_max)
