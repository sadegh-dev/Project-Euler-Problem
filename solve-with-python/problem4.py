"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
999 * 998
999 * 999
"""

z = 0
goal = [0,0,0]

flag = False
for x in range(999,100,-1):
    for y in range(999,100,-1):
        z = str(x*y)
        if len(z) == 6:
            if (z[0] == z[-1]) and (z[1] == z[-2]) and (z[2] == z[-3]):
                flag = True
                break
        else:
            if (z[0] == z[-1]) and (z[1] == z[-2]) :
                flag = True
                break
    if flag :
        z = int(z)
        if goal[0] < z :
            goal[0] = z
            goal[1] = y
            goal[2] = x

 

print (f'{goal[0]} = {goal[1]} * {goal[2]}')