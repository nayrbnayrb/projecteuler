#!/usr/bin/env python

# Find the sum of numbers in the crosses in a 1001 by 1001 spiral

i = 2 # how much the next number is incremented by
number = 1 # The current red number
aggro = 1 # 

while i < 1001: # +2+2+2+2,+4+4+4+4,...+1000+1000+1000+1000
	adding = 4 * number
	adding2 = 10 * i
	print "i = " + str(i) + " adding = " + str(adding) + " adding2 = " + str(adding2)
	aggro += 4 * number + 10 * i # adding 4 more numbers, each incremented by i
	number += 4 * i
	i += 2

print aggro

#	print 8 * ((500^2) + 500)/2
# Really this is 8((500)^2 + 500)/2
# No, not really...

