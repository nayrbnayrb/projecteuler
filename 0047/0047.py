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

def has_distinct_factors(n,f): # Number, returns a list of the factors, with 0: the number
	# Find all prime factors for i and put them in a[i]
	factors = {}
	factors[0] = n
	leftover = n
	while(leftover % 2 == 0):
		leftover /= 2
		if 2 in factors:
			factors[2] += 1
		else:
			factors[2] = 1
	divisor = 3
	if f == 4:
		largest_possible_prime = int(i/(2*2*3*5)) # This assumes multiple of 4
	else:
		largest_possible_prime = int(i/(2))
	# This means prime numbers will not appear solo, as they are >number/2
	# But wait...All of the numbers we're looking for have at least 4 prime factors!
	# So 2*3*5*7!  So the largest possible prime is at most number/(2*3*5)!

	while divisor <= largest_possible_prime:
		if(is_prime(divisor)):
			if(leftover % divisor == 0):
				leftover /= divisor
				if divisor in factors:
					factors[divisor] += 1
				else:
					factors[divisor] = 1
			if(leftover % divisor == 0):
				continue
		divisor +=2
		if(leftover == 1):
			break

	return factors
	
# Goal: Find the first 4 consecutive integers to have four distinct prime factors...
# First, try to find 4 consecutive integers which have 4 prime factors each
# Thinking about it, these might be equivalent...

MAX = 900000

# This is too slow...
# Ideas to make it faster...
# 1) Don't store the numbers...Just have a counter for the consecutive number of 4s
# 2) Funroll loop for finding divisor to 2/6 instead of 1/2
# 3) Speed up by factor of 4 by only checking each fourth, and if it is, then checking those around it...
# 4) Do this for multiples of 4, to give you a head start with two twos?
# ...If this does indeed go by n^2, then this gives you a factor of 4 as well as a factor of 16?!?
# Maybe not quite...
i = 4

while i < MAX:
	# Find all prime factors for i and put them in a[i]
	a = [{} for x in range(8)]
	factors = has_distinct_factors(i,4)
	if len(factors) == 5:
		a = [{} for x in range(8)]
		a[3] = has_distinct_factors(i-1,4)
		a[4] = factors
		a[5] = has_distinct_factors(i+1,4)
		if len(a[3]) == 5:
			a[1] = has_distinct_factors(i-3,4)
			a[2] = has_distinct_factors(i-2,4)
		if len(a[5]) == 5:
			a[6] = has_distinct_factors(i+2,4)
			a[7] = has_distinct_factors(i+3,4)
		factor_sum = 0
		for j in range (1,8):
			if len(a[j]) == 5:
				factor_sum += 1
		if factor_sum > 3:
			for k in range (1,8):
				if len(a[k]) == 5:
					print a[k]
			print
	i += 4

print MAX

# Why did I never find the following before?  Because it was too slow, and I never went from 90k to 900k! :D

#{0: 134043, 3: 1, 491: 1, 13: 1, 7: 1}
#{0: 134044, 47: 1, 2: 2, 31: 1, 23: 1}
#{0: 134045, 17: 1, 83: 1, 19: 1, 5: 1}
#{0: 134046, 11: 1, 2: 1, 3: 2, 677: 1}

