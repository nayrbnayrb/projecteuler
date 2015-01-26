#!/usr/bin/env python
# This function is based on: http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
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

number = 600851475143
divisor = 3
largest_possible_prime = int(number**0.5)
leftover = number

while divisor <= largest_possible_prime:
	if(is_prime(divisor)):
		if(leftover % divisor == 0):
			leftover /= divisor
			print "divisor is " + str(divisor)
			print "leftover is " + str(leftover)
	divisor +=2
	if(leftover == 1):
		break
