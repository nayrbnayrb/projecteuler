#!/usr/bin/env python

accumulator = 0

SIZE = 28123 + 1

x = [0 for i in range(SIZE)]
abundant_numbers = ["" for i in range(SIZE)]
abundant_number_sums = [False for i in range(SIZE)]

# Find All the abundant numbers

i = 1
j = 1
k = 0

while i < SIZE:
	j = 1
	while j <= i/2:
		if i % j == 0:
			x[i] += j
		#print x
		j +=1
	if x[i] > i:
		abundant_numbers[k] = i
		k += 1
#		print "i = " + str(i) + " abundance = " + str(x[i])
	i +=1

# Find all the sums of abundant numbers

print k

i = 0
j = 0

while i < k:
	j = 0
	while j <= i:
		foo = abundant_numbers[i] + abundant_numbers[j]
		if foo < SIZE:
			abundant_number_sums[foo] = True
		j += 1
	i += 1

print abundant_number_sums

# Sum the rest of the numbers from 1 to 28123

i = 1

accum = 0

while i < SIZE:
	if not abundant_number_sums[i]:
		accum += i
	i += 1
print accum



