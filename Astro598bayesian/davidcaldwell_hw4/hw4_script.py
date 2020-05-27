#!/sw/anaconda3-4.2.0/bin/python

# DJC - hw_4 script

# import bayesian functions module
import bayesian_functions_hw4 as bf

# define a,b in list of lists
a_b_vec = [[1,1],[20,20],[20,1],[1,20]]

# generate plots
[bf.plot_beta_func(x,y) for [x,y] in a_b_vec]
