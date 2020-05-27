import numpy as np
import matplotlib.pyplot as pl 

def sOfn(p,n):
    return 1/((1-p)+(p/n))
    
    
p = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
n = range(1,65536)

for i in p:
    pl.figure()
    iRange = [i]*len(n)
    a = map(sOfn,iRange,n)
    aMax = max(a)
    aMaxList = [aMax]*len(a)
    eps = 0.05*aMax
    difference = np.array(aMaxList) - np.array(a)
    procMinApprox = np.where(difference<=eps)[0][0]
    print ('Approximate number of processors required for 95% of maximum speed up ' + str(procMinApprox))

    pl.plot(n,a,label=('p = ' + str(i)))
    
    pl.legend(loc=4)
    pl.ylabel('run time speed up')
    pl.xlabel('log base 2 number of processors')
    pl.title('Run time speed up vs. # of processors for p =' + str(i))
    fig = pl.gcf()
    pl.xscale('log',basex=2)
    fig.set_size_inches(5,5)   

pl.figure()
for i in p:
    iRange = [i]*len(n)
    a = map(sOfn,iRange,n)
    pl.plot(n,a,label=('p = ' + str(i)))

pl.legend(loc=4)
pl.ylabel('run time speedup')
pl.xlabel('log base 2 number of processors')
pl.title('Run time speed up vs. # of processors for various values of p')
fig = pl.gcf()
pl.xscale('log',basex=2)
fig.set_size_inches(10,10)   
plt.rcParams.update({'axes.titlesize': 'small'})

