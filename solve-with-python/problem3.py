"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143  ?
"""

goal = 600851475143

pf = [2] #prime factors
mypf = [] #prime factors of goal

if goal % 2 == 0 :
	mypf.append(2)

for x in range(3,goal) :
	flag_pf = True
	for y in pf:
		if x % y == 0 :
			flag_pf = False
			break	
	
	if flag_pf :
		pf.append(x)
		if goal % x == 0 :
			mypf.append(x)


#print (pf)
#print (mypf)
print (mypf[-1])