#!/sw/anaconda3-4.2.0/bin/python

# DJC - this is the script that runs the coinflip program for astro 598 bayesian
# statistics hw 1.
# requires anaconda distribution (or similar) to be loaded
#

# import coinflip module
import coinflip as cfm

# Part a

cfm.coinflip_func(0.2,1000,5000)

# Part b
p = 0.3
N = [8,16,32,64,128]
M = 1000

[cfm.coinflip_func(0.3,x,M) for x in N]

# part c

p = 0.03
N = [10,100,1000,10000]
M = 1000

[cfm.coinflip_func(0.3,x,M) for x in N]
