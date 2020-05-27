import bayesian_estimation_functions as bef
import bayesian_functions as bf

# generate data.out if it's not already there

#-----------------------------------------------#
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

#-----------------------------------------------#
# hw 3 part

# part b
bef.findMAPestimate('kpost.out')

# part d
bef.findCredibleInterval('kpost.out')

# part f
bef.findMeanEstimate('kpost.out')
