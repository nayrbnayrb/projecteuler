#!/usr/bin/env python

SIZE = 10000

x = [0 for i in range(SIZE)]

i = 1

while i < SIZE:
	j = 1
	while j <= i/2:
		if i % j == 0:
			x[i] += j
		#print x
		j +=1
	print i
	i +=1

i = 1
accum = 0

while i < SIZE:
	if x[i] <SIZE and x[i] > i and x[x[i]] == i:
		accum += i
		accum += x[i]
		print accum
	i += 1
