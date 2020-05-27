#!/usr/bin/python 

import mergeSort
import random 
import sys 

whichN = int(sys.argv[1])

N = [10**2, 10**4, 10**6, 10**8]

i = N[whichN]

randArray = [random.randint(1,10000) for j in range(0,i)]

mergeSort.mergeSort(randArray)


