#!/usr/bin/env python

def is_prime(n):
    if(n==2 or n==3): return True
    if(n % 2 == 0): return False
    if(n % 3 == 0): return False
    if(n < 2): return False
    if(n < 9): return True
    maxpossible = int(n**0.5)
    f = 5
    while f <= maxpossible:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f+=6
    return True

# "Goldbach's other conjecture"

# "What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"

import math

i = 9
j = 1

while i < 10000:
	# Make sure it's composite
	if is_prime(i):
		i += 2
		continue
	# Check to see if it can be written as the sum of a prime and twice a square
	# try all squares up to sqrt(i/2)
	j = 1
	found = False
	while j < (math.sqrt(i/2)+1):
		check = (i - 2*j*j)
		if check < 0:
			break
		if is_prime(i - 2*j*j):
			found = True
			break
		j += 1
	if found == False:
		print "Found nought! i = " + str(i)
	i += 2



