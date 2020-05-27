#!/usr/bin/python 


# This code is for problem one from Astro 598
# Monte Carlo methods for Computational Science 

import numpy as np
import matplotlib.pyplot as plt
import poissonPDF
import gaussianPDF

# problem 1

lamb = [0.5,2,4,8]
n = list(range(0,11))
p0 = [poissonPDF.poissonPDF(i,lamb[0]) for i in n]
p1 = [poissonPDF.poissonPDF(i,lamb[1]) for i in n]
p2 = [poissonPDF.poissonPDF(i,lamb[2]) for i in n]
p3 = [poissonPDF.poissonPDF(i,lamb[3]) for i in n]

plt.figure(1)
plt.plot(n,p0,'bo',n,p1,'ro',n,p2,'go',n,p3,'ko')
plt.ylabel('Probability')
plt.xlabel('n')
plt.title('Poisson probability distribution function')
label = ['lambda = 0.5','lambda = 2','lambda = 4','lambda = 8']
plt.legend(label,numpoints=1)

# problem 2 

mu = 0
sigma = [0.5,2,4,8]

t = np.arange(-10.,10.,0.1)

g0 = [gaussianPDF.gaussianPDF(i,mu,sigma[0]) for i in t]
g1 = [gaussianPDF.gaussianPDF(i,mu,sigma[1]) for i in t]
g2 = [gaussianPDF.gaussianPDF(i,mu,sigma[2]) for i in t]
g3 = [gaussianPDF.gaussianPDF(i,mu,sigma[3]) for i in t]

plt.figure(2)
plt.plot(t,g0,'b',t,g1,'r',t,g2,'g',t,g3,'k')
plt.ylabel('Probability')
plt.xlabel('t')
plt.title('Gaussian probability distribution function')
label = ['sigma = 0.5','sigma = 2','sigma = 4','sigma = 8']
plt.legend(label)
