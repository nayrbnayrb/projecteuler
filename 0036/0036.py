#!/usr/bin/env python

#print bin(35)
#print str(bin(35))[0]
#print str(bin(35))[1]
#print str(bin(35))[2]
#print str(bin(35))[3]
#print str(bin(35))[4]
#print str(bin(35))[5]
#print str(bin(35))[6]
#print str(bin(35))[7]

#print str(bin(35))[2:]


def is_palindrome(n):
	s = str(n)
	if n<1:
		return False
	if len(s) == 1:
		return True
	while len(s) >1:
		if s[0] == s[-1]:
			s = s[1:-1]
			next
		else:
			return False
	return True 

aggro = 0

for n in range (1,1000000):
	if is_palindrome(n):
		if is_palindrome(str(bin(n))[2:]):
			print "n = " + str(n) + " bin(n) = " + str(bin(n))[2:]
			aggro += n


print aggro
