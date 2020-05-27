#!/sw/anaconda3-4.2.0/bin/python

# DJC - this is the script that does bayesian estimation with a flat prior
# requires anaconda distribution (or similar) to be loaded


# import bayesian functions module
import bayesian_functions as bf

# define N and theta
N = 100
theta = 0.2

# generate data.out file
bf.make_data_flips(N,theta)

# read in generated file, create posterior density based off of gridded theta
# values
bf.makekposterior('data.out')

# read in kpost.out, plots posterior probability as a function of theta
bf.plotkposterior('kpost.out')
