T = int(input())

count = 0
num = T

while True:
    if num % 5 == 0:
        
        count += num//5
        break
    else:
        if num >= 3:
            num -= 3
            count += 1
        else:
            count = -1
            break

print(count)