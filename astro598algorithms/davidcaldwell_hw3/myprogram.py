#!/usr/bin/python
# HW3 - astro598 algorithms 
# David Caldwell

import random
import stack

print("Implementing stack")

S = stack.Stack()

print("Pushing 10 random numbers to stack")

for i in range(1,11):
    
    #random integers drawn from 1 to 1000
    j = random.randint(1,1000)
    print("Pushing {0} onto the stack".format(j))
    S.push(j)
    
for i in range(1,11):
    
    a = S.pop()
    print("Popping {0} off the stack".format(a))
    
    