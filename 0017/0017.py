#!/usr/bin/env python

# Sum of number of letter in the words from 'one' to 'one thousand'

# Two methods:
# Figure out how many from one to one hundred, then add stuff

a = ["" for x in range(1001)]

a[0] = ''
a[1] = 'one'
a[2] = 'two'
a[3] = 'three'
a[4] = 'four'
a[5] = 'five'
a[6] = 'six'
a[7] = 'seven'
a[8] = 'eight'
a[9] = 'nine'
a[10] = 'ten'
a[11] = 'eleven'
a[12] = 'twelve'
a[13] = 'thirteen'
a[14] = 'fourteen'
a[15] = 'fifteen'
a[16] = 'sixteen'
a[17] = 'seventeen'
a[18] = 'eighteen'
a[19] = 'nineteen'
a[20] = 'twenty'
a[30] = 'thirty'
a[40] = 'forty'
a[50] = 'fifty'
a[60] = 'sixty'
a[70] = 'seventy'
a[80] = 'eighty'
a[90] = 'ninety'
a[100] = 'hundred'
a[1000] = 'thousand'

word_and = 'and'

i = 1

accum = 0

while i <= 1000:
	if i % 100 < 20:
		accum += len(a[i%100])
	else:
		accum += len(a[i%10])
		accum += len(a[((i%100)/10)*10])
	if i % 10000 >= 1000:
		accum += len(a[1000])
		accum += len(a[(i%10000)/1000])
	if i % 1000 >= 100:
		accum += len(a[100])
		accum += len(a[(i%1000)/100])
		if i%100 >=1:
			accum += len(word_and)
	print "i = " + str(i) + " accum = " + str(accum)
	i += 1
