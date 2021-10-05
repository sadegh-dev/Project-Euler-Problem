a = 210 #2*3*5*7
flag = True
while flag:
    a +=1
    m = 0
    for x in range(1,21):
        m = a % x
        if m != 0:
            break
    else:
        flag = False 
    

print (a)