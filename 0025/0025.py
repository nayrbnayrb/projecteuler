#!/usr/bin/env python

i = 3
fm2 = 1
fm1 = 1
f = 2
while f <= 10**1000:
	if f >= 10**999:
		print "f = " + str(f) + " i = " + str(i)
	temp = f + fm2
	fm1 = fm2
	fm2 = f
	f = temp
	i += 1



