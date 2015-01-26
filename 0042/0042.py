#!/usr/bin/env python

# Coded Triangle Numbers!

import math

f = open('./p042_words.txt', 'r')

trianglewords = 0

SIZE = 2000

x = ["" for i in range(SIZE)]

line = ''

#line = f.readline()
line = f.read()

a = line.split("\",\"")

line.strip

#print a

a = sorted(a)

print a

# Now do the math!  (The monster math...)

i = 0

#print a[0]

numletters = 0

while i < len(a):
#	print "i = " + str(i) + " word = " + a[i]
	j = 0
	lettersum = 0
	while j < len(a[i]):
		lettersum += (ord(a[i][j]) - ord('A') + 1)
			#print accum
		j += 1
	print int(math.sqrt(2 * lettersum))
	print (int(math.sqrt(2 * lettersum))+1)
	if (int(math.sqrt(2 * lettersum)) * (int(math.sqrt(2 * lettersum))+1) == 2 * lettersum): 
		trianglewords +=1
	print "trianglewords = " + str(trianglewords) + " word = " + a[i] + " letter sum = " + str(lettersum)
	i += 1

print numletters

