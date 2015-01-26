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

# Goal is to return the 10001st prime!

goal = 10001
prime_test = 3
prime_ordinal = 2
i = 1
while i == 1:
	prime_test +=2
	if is_prime(prime_test):
		prime_ordinal +=1 
		print "Prime is " + str(prime_test) + " and prime_ordinal is " + str(prime_ordinal)
	if prime_ordinal == 10001:
		break
