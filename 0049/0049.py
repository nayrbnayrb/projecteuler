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

# Find 3 primes which are palindromes of each other which are also equally distant from each other arithmetically
# They are also all 4 digits

# List of all 4-digit primes
# For each two of them, see if the third is also prime

# Accidentally did this one before 0047

a = [0 for x in range(1061)]
j = 0

for i in range (1000,10000):
	if is_prime(i):
		a[j] = i
		j += 1

print a

for i in range (0,len(a)):
	for j in range (i + 1, len(a)):
		check = (a[j] - a[i] ) + a[j]
#		print "i = " + str(a[i]) + " j = " + str(a[j]) + " check = " + str(check)
		if is_prime(check) and check < 10000:
			sum_digits_i = a[i]%10 + (a[i]/10)%10 + (a[i]/100)%10 + (a[i]/1000)
			sum_digits_j = a[j]%10 + (a[j]/10)%10 + (a[j]/100)%10 + (a[j]/1000)
			sum_digits_c = check%10 + (check/10)%10 + (check/100)%10 + (check/1000)
#			print str(sum_digits_i) + " " + str(sum_digits_j) + " " + str(sum_digits_c)
			prod_digits_i = a[i]%10 * ((a[i]/10)%10) * ((a[i]/100)%10) * (a[i]/1000)
			prod_digits_j = a[j]%10 * ((a[j]/10)%10) * ((a[j]/100)%10) * (a[j]/1000)
			prod_digits_c = check%10 * ((check/10)%10) * ((check/100)%10) * (check/1000)
#			print str(prod_digits_i) + " " + str(prod_digits_j) + " " + str(prod_digits_c)
			if sum_digits_i == sum_digits_j and sum_digits_j == sum_digits_c:
				if prod_digits_i == prod_digits_j and prod_digits_j == prod_digits_c:
					print "i = " + str(a[i]) + " j = " + str(a[j]) + " check = " + str(check)


# i = 2969 j = 6299 check = 9629
# The key was the precedence of the mod (%) operator... Was making it miss even the correct one.
