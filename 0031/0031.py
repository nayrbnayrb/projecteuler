#!/usr/bin/env python

# Find all of the different ways to make 200p from the coins:
# 1p,2p,5p,10p,20p,50p,100p,200p

p1p = 0
p2p = 0
p5p = 0
p10p = 0
p20p = 0
p50p = 0
p100p = 0
p200p = 0

aggro = 0

# Basic algo: loop with 8 levels, starting at 0, saying yes and breaking when you hit 200
# (This should get 1x200p and 200x1p

for p200p in range(0,1+1):
	for p100p in range(0,2+1):
		for p50p in range(0,4+1):
			for p20p in range(0,10+1):
				for p10p in range(0,20+1):
					for p5p in range(0,40+1):
						for p2p in range(0,100+1):
							for p1p in range(0,200+1):
								sums = p1p + 2*p2p + 5*p5p + 10*p10p + 20*p20p + 50*p50p + 100*p100p + 200*p200p
								if sums == 200:
								#	print str(p1p)+" "+str(p2p)+" "+str(p5p)+" "+str(p10p)+" "+str(p20p)+" "+str(p50p)+" "+str(p100p)+" "+str(p200p)
									aggro += 1
								elif sums >200:
									break

print aggro

# Also quick, once I remembered to reduce how long the multiloop took

#Congratulations, the answer you gave to problem 31 is correct.
#You are the 45123rd person to have solved this problem.

# Coming close to 10% zone! :D

# (45k have solved this problem, 422k have solved the first problem, even though 11.6% have solved 31 problems, probably nowhere near that many have solved the first 31 problems... :D )
