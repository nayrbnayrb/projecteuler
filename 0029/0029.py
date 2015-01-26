#!/usr/bin/env python

# Find out all the unique numbers a^b for 2<=a<=1000 and 2<=b<=1000

aggro = 0
aggro2 = 0

for a in range(2,101):
	for b in range (2,101):
		n = 2
		while n < (10 + 1):
			print "a = " + str(a) + " b = " + str(b) + " n = " + str(n)
			# If there is a number <= 1000 that you (as a) can power yourself to that also:
				# divides evenly into that power (as b)
			if(a**n <= 100) and ((b % n) == 0) and ((b/n) >= 2):
				print "FOUND a = " + str(a) + " b = " + str(b) + " n = " + str(n)
				print "We think it will collide with: " + str(a**n) +"^" +str(b/n)
				aggro -=1
				aggro2 += 1
				break
			n += 1
		aggro +=1


print aggro
print aggro2

# This is wrong...It seems to be missing a bunch of duplicates...but which ones?  (some second-order effect?)
# But there should only be straight-line effects...

# I think it's missing the a^3/2 type solutions?

# 4^3 seems to be missed...checking...
# Yes!  4^3 == 8^2, but I miss it because it's a fractional difference.  Hooray!
# Teaches me to do the more complicated way, because it's much more difficult to debug when I miss a case...
# (And also how fast computers are...)
# Remember, 1e9 things was fine in 2001...

#a = 30 b = 1000 n = 2
#a = 31 b = 1000 n = 2
#981368
#
#real	35m30.850s
#user	35m29.069s
#sys	0m1.331s
#Bryans-MacBook-Pro:0029 bakeith$ 

