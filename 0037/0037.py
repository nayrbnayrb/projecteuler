#!/usr/bin/env python

# Find the numbers that when you truncate them, from right or left, all numbers left are still primes...

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

# How do you know the max number?  Just count to 11?

# 1e6?  

aggro = 0

for n in range (11,1000000):
	leftn = str(n)
	rightn = str(n)
	right = True
	left = True
	while rightn:
		if not is_prime(int(rightn)):
			right = False
			break
		rightn = rightn[1:]
	if not right:
		next
	while leftn:
		if not is_prime(int(leftn)):
			left = False
			break
		leftn = leftn[:-1]
	
	if right and left:
		aggro += n
		print n
print aggro
