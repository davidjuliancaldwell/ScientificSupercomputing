#!/bin/python
nums = open('input')

odds = list()
evens = list()


for line in nums:
	if line.split():
		integer = int(line.strip())
	
		if (((integer)%2) == 0):
			evens.append(str(integer))
		else:
			odds.append(str(integer))


inputEven = open('input.even','w')
inputOdd = open('input.odd','w')

inputEven.seek(0)
inputOdd.seek(0)

inputEven.write(str(evens))
inputOdd.write(str(odds))

nums.close()
inputEven.close()
inputOdd.close()


