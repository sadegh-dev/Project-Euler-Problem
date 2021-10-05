i = 1
j = 2
fibo = [2]
sumi = 0
sumj = 2
while (i+j) <= 4000000 :
	sumi = i+j
	if sumi % 2 == 0 :
		fibo.append(sumi)
		sumj += sumi
	i = j
	j = sumi
print ("Fibonacci even-valued : " + str(fibo))
print ("sum even-valued : " + str(sumj))