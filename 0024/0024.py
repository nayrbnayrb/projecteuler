#!/usr/bin/env python

# This one is an interesting exercise in factorials...

# There are a total of 10! permutations here...

# The first 9! of them start with 0

import math

# 0! 	 1  
# 1! 	 1
# 2! 	 2
# 3! 	 6
# 4! 	 24
# 5! 	 120
# 6! 	 720
# 7! 	 5040
# 8! 	 40320
# 9! 	 362880
#10! 	 3628800

i = 1

left_over = 1000000

while i <=10:
	subtraction = (left_over/math.factorial(10-i))
	if subtraction > 0:
		left_over -= math.factorial(10-i) * (left_over/math.factorial(10-i))
	print subtraction
	i += 1

print left_over

# The output below shows:

# 0,1,2,3,4,5,6,7,8,9
# 8 5 0 3 9 6 1 2 4 7

# 2673815904 Wrong, because this conts inclusively from 0...

# 0,1,2,3,4,5,6,7,8,9
# 8 5 0 3 6 7 9 1 2 4

# 2783914506

# Then you go back one, because the 1000000 adds one

# 2783914065 No!

# manually:
# 2783915460

# I got the #2 wrong, which was 5 instead of 4, then it spiraled from there....

# (0,1,2::0,1,3,4,5,6::0,1,3,4,5,7::0,1,3::0,1,4,5,8::0,1:: etc...

#Bryans-MacBook-Pro:0024 bakeith$ python 0024.py 
#2
#6
#6
#2
#5
#1
#2
#2
#0
#0
#0
#Bryans-MacBook-Pro:0024 bakeith$ 
