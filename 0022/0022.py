#!/usr/bin/env python

f = open('./p022_names.txt', 'r')

accum = 0

SIZE = 6000

x = ["" for i in range(SIZE)]

line = ''

#line = f.readline()
line = f.read()

a = line.split("\",\"")

line.strip

#print a

a = sorted(a)

print a

# Now do the math!  (The monster math...)

i = 0

#print a[0]

numletters = 0

while i < len(a):
	print "i = " + str(i) + " name = " + a[i]
	j = 0
	while j < len(a[i]):
		if (ord(a[i][j]) >= ord('A') and ord(a[i][j]) <= ord('Z')):
			accum += (ord(a[i][j]) - ord('A') + 1) * (i + 1)
			print (ord(a[i][j]) - ord('A')+1) * (i+1)
			numletters +=1
			#print accum
		j += 1
	i += 1
	print accum

print accum
print numletters
#print len(a)
#print a[0][0]
#print a[0][1]
#print a[0][2]
#print a[0][3]
#print a[0][4]
