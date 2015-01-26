#!/usr/bin/env python

aggro = 0

for i in range(1,1000):
	if (i % 5 == 0 or i % 3 == 0):
		aggro += i
		print "sum is " + str(aggro) + " and i is " + str(i)
