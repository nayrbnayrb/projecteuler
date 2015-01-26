#!/usr/bin/env python

# Time to count some Sundays...

# A few options: 
# There are only 14 different years...
# Go month by month... Let's try this...


year = 1901
month = 1
dayofweek = 2 # Tuesday is Jan 1 1901

numsundays = 0

while year <=2000:
	month = 1
	while month <= 12:
		if dayofweek == 0:
			numsundays += 1
		if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			dayofweek = (dayofweek + 31) % 7
		elif month == 4 or month == 6 or month == 9 or month == 11:
			dayofweek = (dayofweek + 30) % 7
		elif month == 2:
			if year % 4 == 0:
				dayofweek = (dayofweek + 29) % 7
			else:
				dayofweek = (dayofweek + 28) % 7
		month += 1
	year +=1
	print numsundays

print "numsundays = " + str(numsundays)
