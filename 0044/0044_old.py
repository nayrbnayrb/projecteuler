#!/usr/bin/env python

# Pentagon Numbers:
# Find pairs of pentagonal numbers (Pn == n*(3*n-1)/2)
# which are separated by another pentagonal number...
# and sum to another pentagonal number

# Minimize their difference

MAX = 10000

def pentagonal(n):
	return n*(3*n-1)/2


# Perhaps the most interesting part here is the algorithm to iterate in a triangular fashion, so we don't have the halting problem issue...
# (Similar to how we order orbitals in chemistry...

def is_pentagonal(n):
	g = 1
	while g < MAX * 2:
		if n == g * (3*g-1)/2:
			return True
		g += 1
	return False

# Thinking about it, there is a way to do it in half the time, but that is an unnecessary optimization
i = 1
j = 1

# Well, the below isn't working at all (or at least, at all fast...)

# So, let's use the fact that for the difference between pentagonal(n) and pentagonal(n+m) = (4mn+m^2)/2

# And for difference pentagon p:

# (4mn+m^2)/2 = p(3p-1)/2

# 4mn + m^2 = p(3p - 1)

# So, cycle through m & n as below, and test (4mn+m^2)/2 to see if it's pentagonal!

# if j = m and i = n...

while j < MAX:
	if is_pentagonal((4*j*i + j*j)/2):
		print "Found one! n = " + str(i) + " n+m = " str(i+j)



	if j==1:
		j = i + 1
		i = 1
	else:
		i += 1
		j -= 1



while j < MAX:
	a = False
	b = False
#	print str(i) + " " + str(j) + " " + str(pentagonal(i)) + " " + str(pentagonal(j))
	x = "i = " + str(i) + " j = " + str(j) + " sum = " + str(abs(pentagonal(i) + pentagonal(j))) + " is_pentagonal = " + str(is_pentagonal(abs(pentagonal(i) + pentagonal(j))))
	y = "i = " + str(i) + " j = " + str(j) + " diff = " + str(abs(pentagonal(i) - pentagonal(j))) + " is_pentagonal = " + str(is_pentagonal(abs(pentagonal(i) - pentagonal(j))))
	if is_pentagonal(abs(pentagonal(i) + pentagonal(j))):
		a = True
		print x
	if is_pentagonal(abs(pentagonal(i) - pentagonal(j))):
		print y
		b = True
	if a and b:
		print "Found one!"
	# If pentagonal(i) + pentagonal(j) == pentagonal:
#	if (is_pentagonal(abs(pentagonal(i) + pentagonal(j)))):
#		print "sum of " + str(pentagonal(i)) +" and " + str(pentagonal(j)) + " is pentagonal!"
#		# If abs(pentagonal(i) - pentagonal(j)) == pentagonal
#		if (is_pentagonal(abs(pentagonal(i) - pentagonal(j)))):
#			print "difference of " + str(pentagonal(i)) +" and " + str(pentagonal(j)) + " is pentagonal!"
#			min_pentagon = abs(pentagonal(i) - pentagonal(j))
	if j==1:
		j = i + 1
		i = 1
	else:
		i += 1
		j -= 1
