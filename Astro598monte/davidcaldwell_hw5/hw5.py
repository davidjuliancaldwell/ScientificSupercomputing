import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt

# define probability function
def p_x(x):
    
    prob = np.exp(-(x+6)*(x+6)/2) + np.exp(-(x-6)*(x-6)/2)
    
    return prob
    
# make linearly spaced vector for plotting
n = np.arange(-20,20,0.001)

# used numpy to vectorize the function to work with numpy.arange
vecp_x = np.vectorize(p_x)

# plot the probability distribution 
plt.figure(1)
plt.subplot(221)
plt.plot(n,vecp_x(n),lw=4)
plt.ylabel('P(x)')
plt.xlabel('x')
plt.title('Probability Distribution P(x)')

# set initial conditions
delta = 1
x_initial = 5
N = 10000

# metropolis algorithm

def metropolis(delta,x_initial,N):
    
    x = x_initial
    y = p_x(x)
    x_vec = []
    for i in range(1,N+1):
        s = np.random.uniform(-delta,delta)
        x_new = x+s
        y_new = p_x(x_new)
        
        # Metropolis
        if (y_new > y):
            x = x_new
            y = y_new
        else:
            r = np.random.uniform(0,1)
            
            if(y_new/y > r):
                x = x_new
                y = y_new
        
        x_vec.append(x)
    return x_vec
        

# vectorize metropolis
binwidth = 0.2
# part c
delta = 1
x_initial = 5
N = 10000

x_c = metropolis(delta,x_initial,N)
plt.subplot(222)
count, bins, ignored = plt.hist(x_c,bins=np.arange(-20,20,binwidth))
plt.ylabel('Count of x')
plt.xlabel('x')
plt.title('delta = 1, x_initial = 5, N = 10000')
# part d
delta = 1
x_initial = -5
N = 10000

x_c = metropolis(delta,x_initial,N)

plt.subplot(223)
count, bins, ignored = plt.hist(x_c,bins=np.arange(-20,20,binwidth))
plt.ylabel('Count of x')
plt.xlabel('x')
plt.title('delta = 1, x_initial = -5, N = 10000')
# part e
delta = 10
x_initial = 5
N = 10000

x_c = metropolis(delta,x_initial,N)
plt.subplot(224)
count, bins, ignored = plt.hist(x_c,bins=np.arange(-20,20,binwidth))
plt.ylabel('Count of x')
plt.xlabel('x')
plt.title('delta = 10, x_initial = 5, N = 10000')

plt.show()