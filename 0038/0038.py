#!/usr/bin/env python

# Pandigital Multiples:
# n * 1, n * 2, n*... concatenated include all digits 1..9

# Find the largest one...

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

a = [0,0,0,0,0,0,0,0,0,0]

import re


for n in range (1,9999):
	a = [0,0,0,0,0,0,0,0,0,0]
	total_length = 0
	number_string = ''
	i = 1
	while total_length <9:
		total_length += len(str(n*i))
		number_string = number_string + str(n*i)
		i += 1
	if total_length != 9:
		continue
		#print "n = " + str(n) + " length == " + str(total_length) + " number_string = " + number_string
		# down to 5249...check if all digits are there
	if not re.match('.*1.*',number_string):
		continue
	# Down to 5177
	if not re.match('.*2.*',number_string):
		continue
	# Down to 3034
	if not re.match('.*3.*',number_string):
		continue
	# Down to 1389
	if not re.match('.*4.*',number_string):
		continue
	# Down to 749
	if not re.match('.*5.*',number_string):
		continue
	# Down to 250
	if not re.match('.*6.*',number_string):
		continue
	# Down to 210
	if not re.match('.*7.*',number_string):
		continue
	# Down to 113
	if not re.match('.*8.*',number_string):
		continue
	# Down to 47
	if not re.match('.*9.*',number_string):
		continue
	# Down to 18
	print "n = " + str(n) + " length == " + str(total_length) + " number_string = " + number_string
		
