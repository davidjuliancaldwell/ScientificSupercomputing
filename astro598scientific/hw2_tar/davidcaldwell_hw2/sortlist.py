#!/bin/python
import sys

n = (sys.argv[1])
n = int(n)

a = sys.stdin.readlines()
a_strip = [temp.strip() for temp in a]
a_int = [int(temp) for temp in a_strip[0:n]]

a_sort = sorted(a_int)

for i in a_sort:
	print i
