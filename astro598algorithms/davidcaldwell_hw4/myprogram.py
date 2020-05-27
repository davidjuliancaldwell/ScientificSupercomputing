#!/usr/bin/python

import random
import queue 

print("Implementing Queue")
q = queue.Queue()

print("Putting random numbers on the Queue")
for i in range(11):
    
    # drawing random variable from 1 -> 10000
    j = random.randint(1,10000)
    print("Putting {0} onto the queue".format(j))
    q.put(j)
    
for i in range(11):
    a = q.get()
    print("Getting {0} from the queue".format(a))
    
