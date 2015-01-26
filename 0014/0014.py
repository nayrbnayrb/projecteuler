#!/usr/bin/env python

i = 1
k = 1

max_chain_length = 0
longest_chain_number = 1

while k < 1000000:
#	print "k = " + str(k)
	chain_length = 1
	i = k
	while i != 1:
		if i % 2 == 0:
			i /=2
		else:
			i = 3*i + 1
		chain_length += 1
#	print "chain_length = " + str(chain_length)
	if chain_length > max_chain_length:
		max_chain_length = chain_length
		longest_chain_number = k
	k += 1

print "max chain length = " + str(max_chain_length) + " from number " + str(longest_chain_number)
