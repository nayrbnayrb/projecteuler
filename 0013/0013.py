#!/usr/bin/env python

f = open('./input.txt', 'r')

accumulator = 0

#while f.readline:
#	number = f.readline()
#	number.strip()
#	accumulator += int(number)

for line in open('input.txt'):
	if line.strip:
		n = int(line)
		accumulator += n

print accumulator

