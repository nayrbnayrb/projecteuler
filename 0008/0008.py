#!/usr/bin/env python

# Goal is to find the largest number from multiplying 13 consecutive digits in:

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# Grab the multiplicand of the first 13 digits.  Then multiply by the next, divide by the first (don't divide by zero)
# If you find a zero, fast forward to after the zero

print number * 2

s = str(number)

print s

print s[0]

initial_value = int(s[0]) *int(s[1]) *int(s[2]) *int(s[3]) *int(s[4]) *int(s[5]) *int(s[6]) *int(s[7]) *int(s[8]) *int(s[9]) * int(s[10]) * int(s[11]) * int(s[12])

print initial_value

i = 13

print len(s)

max_value = initial_value

j = 12

while j < len(s):
	i = j - 12
	accumulator = 1
	while i <= j:
		accumulator *= int(s[i])
		i += 1
	if accumulator > max_value:
		max_value = accumulator
	j += 1
	print "i = " + str(i) + " j = " + str(j) + " accumulator = " + str(accumulator) + " max_value = "  + str(max_value)

