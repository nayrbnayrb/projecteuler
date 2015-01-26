#!/usr/bin/env python

def is_prime(n):
    if(n==2 or n==3): return True
    if(n % 2 == 0): return False
    if(n % 3 == 0): return False
    if(n < 2): return False
    if(n < 9): return True
    maxpossible = int(n**0.5)
    f = 5
    while f <= maxpossible:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f+=6
    return True

# Which prime, below 1e6, can be written as the sum of the most consecutive primes?

aggro = 0

a = [0 for x in range(79000)]
j = 0

for i in range (1,1000000):
	if is_prime(i):
		aggro += 1
		a[j] = i
		j += 1

print a
print aggro

maxsum = 0
maxnumber = 0

size = len(a)
size = 1000

for i in range (0,size):
	psum = 0
	pnumber = 0
	for j in range(i,size):
		psum += a[j]
		if psum > 1000000:
			break
		if is_prime(psum):
			pnumber = j-i+1
			if pnumber > maxnumber:
				maxsum = psum
				maxnumber = pnumber

print "maxnumber = " + str(maxnumber) + " maxsum = " + str(maxsum)
		
