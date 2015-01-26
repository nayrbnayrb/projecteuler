#!/usr/bin/env python

# Substring divisibility!

# A 0 to 9 digit number (like 1234568790)

# d234 is div by 2
# d345 is div by 3
# d456 is div by 5
# d567 is div by 7
# d678 is div by 11
# d789 is div by 13
# d890 is div by 17

def permute(z): # Inputs a string of integers, and returns the next one in lexicographial sequence
	length = len(z)
	min_num = length # For initial conditions, replacing 123456789->123456798
	min_num_pos = length-1 # For initial conditions, as above
	replaced_number = length
	replaced_number_pos = length-1
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
			for scort in range(0,length):
				for j in range(length-i,length-1):
					if int(z[j]) > int(z[j+1]):
						temp = z[j+1]
						z = z[0:j+1] + z[j] + z[j+2:length]
						z = z[0:j] + temp + z[j+1:length]
#				print "z5 = " + z
			return z
	return ''



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

a = '0123456789'

aggro = 0

while a:
	print a
	if (int(a[1:4])%2 == 0) and (int(a[2:5])%3 == 0) and (int(a[3:6])%5 == 0) and (int(a[4:7])%7 == 0) and (int(a[5:8])%11 == 0) and (int(a[6:9])%13 == 0) and (int(a[7:10])%17 == 0): 
		print a
		aggro += int(a)
	a = permute(a)

print "sum = " + str(aggro)


#9876543201
#9876543210
#sum = 16695334890
