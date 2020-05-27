
import matplotlib
matplotlib.use('Agg')
import math
import numpy as np
import matplotlib.pyplot as plt


def volume4Dsphere(r,N):

    
    in_count = 0
    total_count = 0    
    
    while (total_count < N):
        x0 = np.random.uniform()
        y0 = np.random.uniform()
        z0 = np.random.uniform()
        w0 = np.random.uniform()
        if ((x0**2 + y0**2 + z0**2 + w0**2) <= 1.0):
            in_count = in_count + 1
            
        total_count = total_count + 1 
    
    sub_section = in_count/float(total_count)
    
    dimensions = 4
    scale_factor = 2**dimensions
    
    vol = sub_section*scale_factor
    return vol
# run it 10 times, get average

#volumes = []

N = [10**2, 10**3, 10**4, 10**5]

def runMult(N):
    volumes = []

    for i in range(10):    
        
        vol = volume4Dsphere(1,N)
        volumes.append(vol)
        
    std_dev = np.std(volumes)
    average = np.average(volumes)
    
    return std_dev, average
    
    # below returns the 10 sampled volumes if need be 
    # return volumes
    
# vectorize the function
runMultV = np.vectorize(runMult)

# the first array contains the standard deviations, the second has the mean 

output = runMultV(N)

# plot it
plt.figure(1)
plt.errorbar(N,output[1],yerr=output[0],lw=2)

plt.xscale('log')
plt.xlim(min(N)/10, max(N)*10)

plt.ylabel('Average Volume (with standard deviation)')
plt.xlabel('Number of Points')
plt.title('Plot of mean volume with standard deviation for Monte Carlo Integration')

plt.savefig('hw4Plot')

