#!/usr/bin/env python

total = 1000

c = 997
b = 2
a = 1

while c >= 335:
	b = c - 1
	while ( b > c / 2 ):
		a = 1000 - c - b
		if (a*a + b*b == c*c):
			print "a = " + str(a) + " b = " + str(b) + " c = " + str(c)
			exit
		b -= 1
	c -= 1 
