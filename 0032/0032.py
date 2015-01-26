#!/usr/bin/env python

# Find all the uniqe 'pan-digital product' numbers...

# Where 39 x 186 = 7254, for example...

# What are the limits?

# using a hash set because might be some dupes...

aggro = 0
aggro2 = 0

# First, make a string of all the numbers from 1-9, in order:
# a[2:5] is 345 (from index to 2, to the one before 5

a = '123456789'
s = set()

def permute(z): # Inputs a string of integers, and returns the next one in lexicographial sequence
	length = len(z)
#	print length
	min_num = 9 # For initial conditions, replacing 123456789->123456798
	min_num_pos = 8 # For initial conditions, as above
	replaced_number = 9
	replaced_number_pos = 8
#	print "z = " + z

	# From the end, look for the longest string of ascending (backwards) numbers.  Find the next number, you'll need it later...
	for i in range(1,length):
		if int(z[length-i]) < int(z[length-i-1]):
			next
		else:
			replaced_number = int(z[length-i-1])
			replaced_number_pos = length-i-1
			break
	# From the end, look for the longest string of ascending (backwards) numbers
	for i in range(1,length):
#		print "z[length-i] = " + z[length-i] + " length-i = " + str(length-i) + " min_num = " + str(min_num) + " min_num_pos = " + str(min_num_pos)
		if int(z[length-i]) <= min_num and int(z[length-i]) > replaced_number:
			min_num = int(z[length-i])
			min_num_pos = length-i
		if int(z[length-i]) < int(z[length-i-1]):
			next
		else:
			# Take the smallest of these greater than the found 'replaced number', and swap it with the immediate previous number.
#			print "z1 = " + z + " replaced_number = " + str(replaced_number) + " " + str(replaced_number_pos)
#			print "z1 = " + z + " min_num = " + str(min_num) + " " + str(min_num_pos)
#			print "z1 = " + z + " length-i-1 = " + str(length-i-1) + " z[l-i-1] = " +z[length-i-1] 
			temp = int(z[length-i-1]) #grab the 'replaced number'
#			print "z2 = " + z
			z = z[0:length-i-1] + str(min_num) + z[length-i:length] # put the min_num where replaced_number was
#			print "z3 = " + z
			z = z[0:min_num_pos] + str(temp) + z[min_num_pos+1:length] # put the replaced_number back where min_num was
#			print "z4 = " + z
			# Now sort the rest of them in ascending order (Uses bubble sort, but doesn't matter for small numbers like these)
			for scort in range(0,9):
				for j in range(length-i,length-1):
					if int(z[j]) > int(z[j+1]):
						temp = z[j+1]
						z = z[0:j+1] + z[j] + z[j+2:length]
						z = z[0:j] + temp + z[j+1:length]
#				print "z5 = " + z
			return z
	return ''
# Reporder all subsequent numbers, in order
# 123456 -> 123465
# 123654 -> 124356
# If all numbers are backwards, return false


while a: 
#	print "a = " + a
	for m in range(1,4+1):
		product = int(a[5:])
#		print int(a[0:m])
#		print int(a[m:5])
		if int(a[0:m]) * int(a[m:5]) == product:
			print int(a[0:m])
			print int(a[m:5])
			print int(a[5:])
			if product not in s:
				s.add(product)
				aggro += product
	a = permute(a)
	 

print "product total = " + str(aggro)

