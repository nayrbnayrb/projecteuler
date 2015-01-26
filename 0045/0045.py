#!/usr/bin/env python

# #45!  The second number which is triangular, pentagonal, and hexagonal!

# Luckily, all triangular numbers are all hexagonal!

# For some reason, (N^2 + N)/2 == (2M^2 - M)

# Option 1: Just check all hexagonal numbers for pentagonalness...

# Option 2: Find some relation between hexagonal and pentagonal numbers...

# Pentagon Numbers:
# Find pairs of pentagonal numbers (Pn == n*(3*n-1)/2)
# which are separated by another pentagonal number...
# and sum to another pentagonal number

# Minimize their difference

import math

MAX = 220000

def pentagonal(n):
	return n*(3*n-1)/2

def is_pentagonal(n):
	g = int(math.sqrt(n*2/3))
	#g = 1
	while g < MAX * 2:
		pentagon = g * (3*g-1)/2
		if n == pentagon:
			return True
		elif pentagon > n:
			return False
		g += 1
	return False

# The secret is actually the upper and lower bounds checking on the is_pentagonal() above...
# 2/3 is a loose lower bound, based on the fact that 2n^2 > 2/3(3n^2-n), because n^2 > n for all n > 1

i = 1

while i < MAX:
	hexagon = i*(2*i-1)
	if is_pentagonal(hexagon):
		print str(i) + " " + str(hexagon)
	i +=1

# Searched 2200 numbers and found only hexagonal number 143 (correctly) in 0.043s
# increase the max!
# Searched 22000 numbers and no change in results in 0.083s
# At 220000, found 27693 in 0.534s! (0.535 to 0.580 with printing the hexagon (& triangular and pentagonal) number)
