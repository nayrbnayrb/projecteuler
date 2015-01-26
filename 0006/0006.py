#!/usr/bin/env python

# Find the difference between the sum of squares from 1 to 100 and the square of the sum from 1 to 100

# A hack is to find the areas of the rectangles which represent the part of the large square minus the small squares:

# sum(1-100) of [(sum(1-100) - i) * i]

# Where the outer sum is sum of all the rectangles, the (sum(1-100) -i) is the width, and the *i is the height!

i = 1
aggro = 0

while i <=100:
	summer = ((5050 - i) * i)
	aggro += summer
	print "sum is " + str(aggro) + " summer is " + str(summer) + " i is " + str(i)
	i +=1 

