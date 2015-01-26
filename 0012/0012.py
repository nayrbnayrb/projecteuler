#!/usr/bin/env python

# Goal: Find the smallest triangular number with more than 500 divisors (501 or more)

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

# Took 25.682s in python

# Iterate through triangular numbers:
triangle = 0
i = 1

while i < 12400:
	factors = {}
	triangle += i
	number = triangle
	leftover = number
#	print "i = " + str(i) + " triangle = " + str(triangle)
	while(leftover % 2 == 0):
		leftover /= 2
		if 2 in factors:
			factors[2] += 1
#			print "A number of 2s = " + str(factors[2])
		else:
			factors[2] = 1
#			print "B number of 2s = " + str(factors[2])

	divisor = 3
	largest_possible_prime = int(number/2)

	while divisor <= largest_possible_prime:
		if(is_prime(divisor)):
			if(leftover % divisor == 0):
				leftover /= divisor
				if divisor in factors:
					factors[divisor] += 1
				else:
					factors[divisor] = 1
#				print "divisor is " + str(divisor)
#				print "leftover is " + str(leftover)
			if(leftover % divisor == 0):
				continue
		divisor +=2
		if(leftover == 1):
			break
	
	num_factors = 1
	for key in factors:
#		print "key = " + str(key) + " value = " + str(factors[key])
		num_factors *= (1 + factors[key])
	if(num_factors)>=400:
		print "i = " + str(i) + " number = " + str(number) + " number of factors = " + str(num_factors)

	i += 1
