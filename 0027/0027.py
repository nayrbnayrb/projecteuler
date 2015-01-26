#!/usr/bin/env python

# Find the coefficients (really, their product) which produces the maximum number of primes for:
# n^2 + an + b, for values of n starting with 0

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

a = 1
maxn = 0
maxa = 0
maxb = 0

while a < 1000:
#	print "a = " + str(a)
	b = 2
	while b < 1000:
#		if a == -79:
		#	print "a = " + str(a) + " b = " + str(b)
		n = 0
		while is_prime(n*n + a*n + b):
			n += 1
		if (n - 1) > maxn:
			maxn = n - 1
			maxa = a
			maxb = b
			print "maxn = " + str(maxn) + " maxa = " + str(maxa) + " maxb = " + str(maxb) + " product_ab = " + str(maxa * maxb)
		b += 1
	a *= -1
	if a > 0:
		a += 1




