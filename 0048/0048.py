#!/usr/bin/env python

# What are the last ten digits of:

# 1^1 + 2+2 + ... + 1000^1000

# Well, try brute force...

# Accidentally did this one before 0047

aggro = 0

i = 1

while i <=1000:
	aggro += i**i
	print aggro
	i += 1

