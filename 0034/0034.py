#!/usr/bin/env python

# Find all of the numbers whose factorials of their digits sum to the numbers...
# Example: 145 -> 1! + 4! + 5! = 145

# (Ignore 1! = 1 and 2! = 2)

# First, what is the limit?

# 9! = 362880
# 6 * 9! = 2177280

# So, it's in the 7 digits at the most

# Put it at 9!*8, to clearly bookend it?

aggro = 0

def factorial(n):
	if n == 0:
		return 1
	elif n == 1 or n == 2:
		return n
	elif n == 3:
		return 6
	elif n == 4:
		return 24
	elif n == 5:
		return 120
	elif n == 6:
		return 720
	elif n == 7:
		return 5040
	elif n == 8:
		return 40320
	elif n == 9:
		return 362880

for i in range (3,8*factorial(9) + 1):
	sumdigits = 0
	sumdigits += factorial(i % 10)
	if i >= 10:
		sumdigits += factorial((i/10) % 10)
	if i >= 100:
		sumdigits += factorial(i/100 % 10)
	if i >= 1000:
		sumdigits += factorial(i/1000 % 10)
	if i >= 10000:
		sumdigits += factorial(i/10000 % 10)
	if i >= 100000:
		sumdigits += factorial(i/100000 % 10)
	if i >= 1000000:
		sumdigits += factorial(i/1000000 % 10)
	if i == sumdigits:
		print "i = " + str(i)
		aggro += i

print "sum total = " + str(aggro)
