#!/usr/bin/env python

# Summation of digits of 2^1000

# First, make sure python can handle it:

n = 2**1000

print n
print 
leftover = n
accum = 0

while leftover >0:
	accum += leftover % 10
	leftover /= 10

print accum

