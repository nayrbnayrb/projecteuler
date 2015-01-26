#!/usr/bin/env python

f = open('./input.txt', 'r')

accumulator = 0

SIZE = 15

x = [["" for i in range(SIZE)] for j in range(SIZE)]

i = 0
j = 0

for line in open('input.txt'):
	if line.strip:
		i = 0
		temp_array = line.split()
		print temp_array
		for foo in temp_array:
			x[j][i] = int(temp_array[i])
			i += 1
		j += 1

print x
print

# midpoints = [["" for i in range(SIZE)] for j in range(SIZE)]

# Put into midpoints the max sum from options below
# Dynamic programming ftw!

i = SIZE - 2
j = SIZE - 2

while j >= 0:
	i = j
	while i >=0:
		if x[j+1][i+1] > x[j+1][i]:
			x[j][i] += x[j+1][i+1]
		else:
			x[j][i] += x[j+1][i]
		i -=1
	print x
	print

	j -=1

print x[0][0]
