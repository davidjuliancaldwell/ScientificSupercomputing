import math
import numpy as np
import matplotlib.pyplot as plt


def gaussianPDF(x,mu,sigma):

    gp = (1/(sigma*math.sqrt(math.pi*2)))*math.exp(-(x-mu)**2/(2*(sigma**2)))
    
    return gp

def poissonPDF(n,lamb):
    
    pn = (lamb**n)*(math.exp(-lamb))/math.factorial(n)
    return pn

vG = np.vectorize(gaussianPDF)
vP = np.vectorize(poissonPDF)

#############
plt.figure(1)
TOTAL_NUM_POINTS = 10**6
a = np.random.poisson(10,TOTAL_NUM_POINTS)
binwidth = 1
count, bins, ignored = plt.hist(a,bins=np.arange(0, max(a) + binwidth, binwidth))

n = np.arange(0,max(a)+1,1)

plt.plot(n,TOTAL_NUM_POINTS*vP(n,10),lw=4,color='red')

plt.ylabel('Histogram Count or N*P(n)')
plt.xlabel('n')
plt.title('Histogram of Poisson PDF vs. N*P(N), N=10**6')
label = ['N*P(n)','histogram']
plt.legend(label,numpoints=1)


###############
plt.figure(2)
TOTAL_NUM_POINTS = 100
b = np.random.poisson(10,TOTAL_NUM_POINTS)
binwidth = 1
count, bins, ignored = plt.hist(b,bins=np.arange(0, max(b) + binwidth, binwidth))


n = np.arange(0,max(b)+1,1)


plt.plot(n,TOTAL_NUM_POINTS*vP(n,10),lw=4,color='red')

plt.ylabel('Histogram Count or N*P(n)')
plt.xlabel('n')
plt.title('Histogram of Poisson PDF vs. N*P(n), N=100')
label = ['N*P(n)','histogram']
plt.legend(label,numpoints=1)




#################
plt.figure(3)
TOTAL_NUM_POINTS = 10**6
a = np.random.normal(0,10,TOTAL_NUM_POINTS)
count, bins, ignored = plt.hist(a,bins=np.arange(min(a) - binwidth, max(a) + binwidth, binwidth))

n = np.arange(min(a),max(a),0.001)


plt.plot(n,TOTAL_NUM_POINTS*vG(n,0,10),lw=4,color='red')

plt.ylabel('Histogram Count or N*P(x)')
plt.xlabel('x')
plt.title('Histogram of Gaussian PDF vs. N*P(n), N=10**6')
label = ['N*P(n)','histogram']
plt.legend(label,numpoints=1)



##########

plt.figure(4)
TOTAL_NUM_POINTS = 100
b = np.random.normal(0,10,TOTAL_NUM_POINTS)
count, bins, ignored = plt.hist(b,bins=np.arange(min(b)-binwidth, max(b) + binwidth, binwidth))


n = np.arange(min(b),max(b),0.001)


plt.plot(n,TOTAL_NUM_POINTS*vG(n,0,10),lw=4,color='red')

plt.ylabel('Histogram Count or N*P(x)')
plt.xlabel('x')
plt.title('Histogram of Gaussian PDF vs. N*P(N), N=100')
label = ['N*P(n)','histogram']
plt.legend(label,numpoints=1)
plt.show()
