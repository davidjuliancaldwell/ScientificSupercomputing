#!/usr/bin/python 
import priorityQueue
import random

priQ = priorityQueue.priorityQueue(20)

for i in range(1,priQ.MAX):
    randint = random.randint(1,1000)
    priQ.insert(randint)
    print("Inserted {0} onto Priority Queue".format(randint))
    
print(priQ.a)

for i in range(1,priQ.MAX):
    minimum = priQ.delMin()
    print("Returning {0} from Priority Queue".format(minimum))