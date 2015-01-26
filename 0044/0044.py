#!/usr/bin/env python

# Pentagon Numbers:
# Find pairs of pentagonal numbers (Pn == n*(3*n-1)/2)
# which are separated by another pentagonal number...
# and sum to another pentagonal number

# Minimize their difference

import math

MAX = 2200

def pentagonal(n):
	return n*(3*n-1)/2


# Perhaps the most interesting part here is the algorithm to iterate in a triangular fashion, so we don't have the halting problem issue...
# (Similar to how we order orbitals in chemistry...

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

# The answer:
#Found one! n = 1020 n+m = 2167
#Hooray! :D Number 1 = 1560090 Number 2 = 7042750
#Sum = 8602840 Difference = -5482660
#Found one! n = 9599 n+m = 9999
#real	2m19.446s
# if we only go to 4k, 22s
# If we only go to 3k: 12.8s
# 2.2k: 6.9s

# Thinking about it, there is a way to do it in half the time, but that is an unnecessary optimization
i = 1
j = 1

# Well, the below isn't working at all (or at least, at all fast...)

# So, let's use the fact that for the difference between pentagonal(n) and pentagonal(n+m) = (4mn+m^2)/2

# And for difference pentagon p:

# (4mn+m^2)/2 = p(3p-1)/2

# 4mn + m^2 = p(3p - 1)

# So, cycle through m & n as below, and test (4mn+m^2)/2 to see if it's pentagonal!

# if j = m and i = n...

# Well, that didn't work...why?

# 3n -> 3(n+m), not (3n + m)

# Therefore, 3m^2 + 6mn - m

while j < MAX:
	if is_pentagonal((6*j*i + 3*j*j-j)/2):
		print "Found one! n = " + str(i) + " n+m = " + str(i+j)
		if is_pentagonal((i*(3*i-1)/2) + ((i+j)*(3*(i+j)-1)/2)):
			print "Hooray! :D Number 1 = " + str(i*(3*i-1)/2) + " Number 2 = " + str((i+j)*(3*(i+j)-1)/2)
			print "Sum = " + str((i*(3*i-1)/2) + ((i+j)*(3*(i+j)-1)/2)) + " Difference = " + str((i*(3*i-1)/2) - ((i+j)*(3*(i+j)-1)/2))

	if j==1:
		j = i + 1
		i = 1
	else:
		i += 1
		j -= 1



