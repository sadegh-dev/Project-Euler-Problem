num = 21

flag = True
while flag:
    num +=1
    remaining = 0
    for x in range(2,21):
        remaining = num % x
        if remaining != 0:
            break
    else:
        flag = False 
    

print (num)

