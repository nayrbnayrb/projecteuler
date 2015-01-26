#!/usr/bin/env python

aggro = 0
i = 0
fm2 = 1
fm1 = 1
f = 2
while f <= 4000000:
	print "f = " + str(f)
	if (f % 2 == 0):
		aggro += f
	temp = f + fm2
	fm1 = fm2
	fm2 = f
	f = temp
	print "aggro = " + str(aggro)
print aggro

