#!/usr/bin/env python

# Find out all the unique numbers a^b for 2<=a<=1000 and 2<=b<=1000

aggro = 0
aggro2 = 0

s = set()

for a in range(2,101):
	for b in range (2,101):
		if a**b in s:
			print "a = " + str(a) + " b = " + str(b) + " in s: " + str(a**b)
			aggro2 +=1
			next
		else:
			#print "a = " + str(a) + " b = " + str(b) + " not yet in s: " + str(a**b)
			aggro +=1
			s.add(a**b)


print aggro
print aggro2


#a = 30 b = 1000 n = 2
#a = 31 b = 1000 n = 2
#981368
#
#real	35m30.850s
#user	35m29.069s
#sys	0m1.331s
#Bryans-MacBook-Pro:0029 bakeith$ 

