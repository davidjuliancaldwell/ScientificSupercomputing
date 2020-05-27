#!/usr/bin/python 

import matplotlib.pyplot as plt
import math 


'''
real    0m0.020s
user    0m0.007s
sys     0m0.002s

real    0m0.009s
user    0m0.005s
sys     0m0.003s

real    0m0.008s
user    0m0.005s
sys     0m0.003s

real    0m0.084s
user    0m0.083s
sys     0m0.001s

real    0m0.087s
user    0m0.085s
sys     0m0.002s

real    0m0.084s
user    0m0.083s
sys     0m0.001s

real    0m10.804s
user    0m10.770s
sys     0m0.036s

real    0m10.344s
user    0m10.316s
sys     0m0.030s

real    0m10.887s
user    0m10.853s
sys     0m0.035s

real    25m35.910s
user    25m32.727s
sys     0m3.533s

real    24m36.281s
user    24m33.438s
sys     0m3.026s

real    25m35.712s
user    25m32.604s
sys     0m3.359s


'''

avg0 = (0.02+0.009+0.008)/3
avg1 = (0.084+0.087+0.084)/3
avg2 = (10.804 + 10.344 + 10.887)/3
avg3 = (1535.91+1476.28+1535.71)/3

dataTime = [avg0, avg1, avg2, avg3]

N = [10**2, 10*4, 10**6, 10**8]
NlogN = [i*math.log(i) for i in N]

plt.plot(NlogN,dataTime,'bo')
plt.xlabel('N log (N) (on log scale)',fontsize=16)
plt.ylabel('Average Running time (T, in seconds) (on log scale)',fontsize=16)
plt.title('logLog Plot of running time (s) vs. N log (N)',fontsize=18)
plt.xscale('log')
plt.yscale('log')
fig = plt.gcf()
fig.set_size_inches(8,8)  




