#!/usr/bin/env python

# What is the sum of digits in 100!

i = 1

accum = 1

while i <=100:
	accum *= i
	i +=1

accum2 = 0

while accum>0:
	accum2 += accum%10
	accum /= 10
	print accum, accum2

# Interestingly, there were 24 trailing zeroes (this is how I checked the answer)...
# 11 for 10,20,...,100
# Plus 10 for each ending in 5, and an extra for 25,50,75
