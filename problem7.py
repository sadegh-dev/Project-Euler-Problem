"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

a = [2]
x = 3

while len(a) < 10001 :
    flag = False
    for d in a :
        if x % d == 0 :
            flag = True
            break
    if flag == False :
        a.append(x)
    x += 1

print(a[-1])