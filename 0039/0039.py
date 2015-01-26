#!/usr/bin/env python


# Find the largest one...

c = 3

max_solutions = 0
value = 0

for n in range (6,1000+1):
	num_solutions = 0
	for a in range (1,332):
		c = 3
		for b in range (a+1,499):
			c = n - a - b
			if c < 3:
				break
			#print "n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
			if a*a + b*b == c*c:
				num_solutions +=1
#				print "n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
#				print "Found one! "
	if num_solutions:
		print "n = " + str(n) + " num_solutions = " + str(num_solutions)
	if num_solutions > max_solutions:
		max_solutions = num_solutions
		value = n

print "max solutions = " + str(max_solutions) + " value = " + str(value)
