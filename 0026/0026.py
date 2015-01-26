#!/usr/bin/env python

import decimal

print decimal.getcontext()

PRECISION = 100

decimal.getcontext().prec = PRECISION
print decimal.getcontext()

i = 1
d = 1

maximumd = 0
maximumi = 0

while d < 1000:
	i = 1
	while i<1599:
		if ((10**i) % d) == 0:
			break
		if ((10**i) % d) == 1:
			print "1/" + str(d) +" has a repeating decimal with " + str(i) + " digits."
			if i > maximumi:
				print "d = " + str(d) + " i = " + str(i)
				maximumi = i
				maximumd = d
			break
		i += 1
	d += 1

print "maximumi = " + str(maximumi)
print "maximumd = " + str(maximumd)
