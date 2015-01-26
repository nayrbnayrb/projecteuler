#!/usr/bin/env python

# Find all of the numbers where they are equal to the 5th power of their digits

aggro = 0

# From thinking about it, 355k is more than any of them can be, since:

# 999999 -> 354294
# 9999999 -> 413343
# 99999999 -> 472392

# So any 7 digit number cannot reach 7 digits, and it just gets worse from there...

# So, go through each number, add up the 5th powers of its digits

for n in range(2,355000):
	digits_sum_n = 0
	digits_sum_n += (n % 10)**5
	digits_sum_n += ((n/10) % 10)**5
	digits_sum_n += ((n/100) % 10)**5
	digits_sum_n += ((n/1000) % 10)**5
	digits_sum_n += ((n/10000) % 10)**5
	digits_sum_n += ((n/100000) % 10)**5
	if n == digits_sum_n:
		print n
		aggro += n

print aggro


# Well, that was fast...
# 34mins from directory making to correct submission, including a trip to the bathroom :D

#Bryans-MacBook-Pro:0030 bakeith$ time python 0030.py 
#4150
#4151
#54748
#92727
#93084
#194979
#443839
#
#real	0m0.790s
#user	0m0.767s
#sys	0m0.019s
#Bryans-MacBook-Pro:0030 bakeith$ 
