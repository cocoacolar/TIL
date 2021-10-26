# 1, 7 , 19, 37 61



x = int(input())
n = 1


while True:
    if x == 1:
        print(1)
        break
    elif(3*(n**2)-(3*n)) + 2 <=  x <= (3*((n+1)**2))-(3* (n+1)) + 1:
        print(n+1)
        break
    else:
        n+=1