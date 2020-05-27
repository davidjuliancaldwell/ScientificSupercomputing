import matplotlib.pyplot as plt
import numpy as np
import math

N = [10,20,30,40]
numReps = 10000

def selfAvoid(N):
    
    totalDists = []
    accepted = 0
    
    for i in range (0,numReps):
        x = 0
        y = 0
        z = 0
        
        locs = [[0,0,0]]
        breakDat = False
        for j in range(0,N):
            if j == 0:
                direction = np.random.choice(6,1)    
                
                x_old = 0
                y_old = 0
                z_old = 0 
        
                if direction == 0:
                    y_pos = y
                    x_pos = x + 1
                    z_pos = z 
                elif direction == 1:
                    y_pos = y 
                    x_pos = x - 1
                    z_pos = z 
                elif direction == 2:
                    y_pos = y + 1
                    x_pos = x 
                    z_pos = z 
                elif direction == 3:
                    y_pos = y - 1
                    x_pos = x 
                    z_pos = z 
                elif direction == 4:
                    x_pos = x
                    y_pos = y
                    z_pos = z - 1
                elif direction == 5:
                    x_pos = x 
                    y_pos = y
                    z_pos = z + 1 
                                
            else:
                
                direction = np.random.choice(6,1)
                
                if direction == 0:
                    y_pos = y
                    x_pos = x + 1
                    z_pos = z 
                elif direction == 1:
                    y_pos = y 
                    x_pos = x - 1
                    z_pos = z 
                elif direction == 2:
                    y_pos = y + 1
                    x_pos = x 
                    z_pos = z 
                elif direction == 3:
                    y_pos = y - 1
                    x_pos = x 
                    z_pos = z 
                elif direction == 4:
                    x_pos = x
                    y_pos = y
                    z_pos = z - 1
                elif direction == 5:
                    x_pos = x 
                    y_pos = y
                    z_pos = z + 1 
                
                while ((x_pos == x_old) and (y_pos == y_old) and (z_pos == z_old) ):
                    direction = np.random.choice(6,1)

                    if direction == 0:
                        y_pos = y
                        x_pos = x + 1
                        z_pos = z 
                    elif direction == 1:
                        y_pos = y 
                        x_pos = x - 1
                        z_pos = z 
                    elif direction == 2:
                        y_pos = y + 1
                        x_pos = x 
                        z_pos = z 
                    elif direction == 3:
                        y_pos = y - 1
                        x_pos = x 
                        z_pos = z 
                    elif direction == 4:
                        x_pos = x
                        y_pos = y
                        z_pos = z - 1
                    elif direction == 5:
                        x_pos = x 
                        y_pos = y
                        z_pos = z + 1 
                
            x_old = x
            y_old = y
            z_old = z
                
            x = x_pos
            y = y_pos
            z = z_pos
                    
            if ([x,y,z] in locs or (breakDat == True)):
                breakDat = True
            else: 
                locs.append([x,y,z])
        if not breakDat:
            final_x = x
            final_y = y 
            final_z = z
            accepted = accepted + 1 
            dist = final_x**2 + final_y**2 +final_z**2

            totalDists.append(dist)
        
    distMean = np.mean(totalDists)
    stdDev = np.std(totalDists)
        
    return distMean,stdDev,accepted 

selfAvoidVector = np.vectorize(selfAvoid)

output = selfAvoidVector(N)
                
plt.figure(1)
plt.errorbar(N,output[0],yerr=output[1],lw=1)
plt.plot(N,output[0],'bo')
#plt.xscale('log')
#plt.yscale('log')

plt.ylabel('Distance Squared')
plt.xlabel('Number of Points')
plt.title('Self Avoiding Random Walk')
plt.axis([0,50,0,160])

#plt.savefig('hw5Plot')
                
                
plt.figure(2)
plt.plot(N,output[0],'bo',N,output[0],'b',lw=1)

plt.xscale('log')
plt.yscale('log')

plt.ylabel('log(Distance Squared)')
plt.xlabel('log(Number of Points)')
plt.title('Self Avoiding Random Walk')
plt.axis([8,100,8,100])

slope, intercept = np.polyfit(np.log(output[0]), np.log(N), 1)

print('The slope of the line that fits the data is ' + str(slope))


plt.figure(3)
plt.plot(N,output[2]/float(10000),'bo',N,output[2]/float(10000),'b',lw=1)

#plt.xscale('log')
#plt.yscale('log')

plt.ylabel('Accepted random walks')
plt.xlabel('Number of Points')
plt.title('Self Avoiding Random Walk')
plt.axis([0,50,0,1])
plt.show()

                    
    
    

