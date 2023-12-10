# Project Euler >> Problem 1
# Title: Multiples of 3 and 5
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Reference: https://projecteuler.net/problem=1

def Multiples_of_3_and_5(num):
	counter = 0
	sum_result = 0
	if(num<3):
		result = "[ ]"
	else:
		result=[]
		for i in range(3,num):
			if(i%3 == 0 or i%5 == 0):
				result.append(i)
				sum_result += i
				counter = counter+1
	print(result)
	print("Multiples is: ",sum_result)

inputt = 1000
Multiples_of_3_and_5(inputt)