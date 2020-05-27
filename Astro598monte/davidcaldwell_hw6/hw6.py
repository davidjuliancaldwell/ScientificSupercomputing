import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt

N = [10**2, 10**3, 10**4]



def randomWalk(N):
    
    totalDists = []
    
    
    for i in range(0,100):
        x0 = 0
        y0 = 0
        
        x = x0
        y = y0
        
        for j in range(0,N):
            direction = np.random.choice(4,1)
            
            if direction == 0:
                y = y
                x = x + 1
            elif direction == 1:
                y = y + 1
                x = x
            elif direction == 2:
                y = y
                x = x - 1
            elif direction == 3:
                y = y - 1
                x = x 
        
        final_x = x
        final_y = y
        
        dist = final_x**2 + final_y**2
        
        totalDists.append(dist)
    
    aveDist = np.mean(totalDists)
    stdDist = np.std(totalDists)
    
    return aveDist,stdDist

randomWalkVector = np.vectorize(randomWalk)

    
output = randomWalkVector(N)

plt.figure(1)
plt.errorbar(N,output[0],yerr=output[1],lw=4)

#plt.xscale('log')
#plt.yscale('log')

plt.ylabel('Distance Squared')
plt.xlabel('Number of Points')
plt.title('Markov Chain Random Walk')
plt.show()

#plt.savefig('hw5Plot')
