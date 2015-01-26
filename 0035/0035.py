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

# Program to find all circular primes below 1e6

# There's a math way and a string way to do the rotation...Let's do the math way...

# Mod 10 to get the remainder
# Div 10 to get the first part to add
# 

import math

#print math.log10(2)

#print int(math.log10(200)/1)

aggro = 0

for faken in range (2,1000000):
	n = faken
	d = 0
	len_check = 0
	length = int(math.log10(faken)) +1
#	print "faken = " + str(faken) + " log(faken) = " + str(int(math.log10(faken)))
	while d < length:
		#print n
		if is_prime(n):
			len_check += 1
		n = n%10*10**int(math.log10(n)) + n/10
		d += 1
	if len_check == length:
		aggro += 1
		print "Found one! " + str(faken)

print "There are " + str( aggro) + " circular primes!"
