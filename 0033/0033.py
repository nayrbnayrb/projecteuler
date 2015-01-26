#!/usr/bin/env python

# Find all of the fractions of the form:

# 49/98, cross out the 9s, then it's still correct! :D

# Go through all options for n/d, for n<d, and n,d >0

for d in range (2,9+1):
	for n in range (1,d-1):
		for c in range (1,9+1):
			if abs(float(n)/float(d) - (float(c)*10.0+float(n))/(float(d)*10 + float(c))) <0.00000000000000000000000000000000000001:
				print abs(float(n)/float(d) - (float(c)*10.0+float(n))/(float(d)*10 + float(c))) 
				print "Found a possible: " + str(c) + str(n) + "/" + str(d) + str(c)
			if abs(float(n)/float(d) - (float(n)*10.0+float(c))/(float(c)*10 + float(d))) <0.00000000000000000000000000000000000001:
#				print abs(float(n)/float(d) - (float(n)*10.0+float(c))/(float(c)*10 + float(d))) 
				print "Found a possible: " + str(n) + str(c) + "/" + str(c) + str(d)

#Found a possible: 16/64
#Found a possible: 19/95
#Found a possible: 26/65
#Found a possible: 49/98

# 387296/38729600 (lol)

# 0.1: 121
# 0.01: 8
# 0.001:4 
# Out to 0.000000000000000001: Still 4
# Out to 0.00000000000000000000000000000000000001: Still 4
# Becuase gives 0.0!
# Also, all of them are in the second check...Why?
# Because it requires the crossed out number to be the end of the denominator?  And that needs to change?
# Wonder if that holds true for other silly examples, with more digits...
