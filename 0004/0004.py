#!/usr/bin/env python

# Find the largest palindromic number made from 2 three-digit numbers:

# Define a 6-digit palindrom finding function:

def is_6digit_palindrome(n):
	if (n / 100000 == n % 10):
		if (((n / 10000) % 10) == n % 100 /10):
			if (((n / 1000) % 10)== n % 1000 /100):
				return True
	return False

# We'll assume it's a 6-digit number, so we'll start with 317^2

i = 317
j = 317
max_num = 0

while i <=999:
	while j <=i:
		k = i * j
		if is_6digit_palindrome(k):
			print i,j,k
			if k > max_num:
				max_num = k
		j += 1
	j = 317
	i += 1

print "max_num = " + str(max_num)


