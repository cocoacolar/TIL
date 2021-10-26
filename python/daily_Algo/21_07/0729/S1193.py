import math
T  = int(input())

numbers = []
for i in range(T):
    x = int(input())
    numbers.append(x)


for x in range(T):
    count = 0
    result = 0
    if numbers[x] > 81:
        print(f'#{x+1} No')
    else:
        for y in range(1, 10):
            if numbers[x] % y == 0 and (numbers[x]//y) < 10:
                result = 1
                
            else:
                count = 1
    if count == 1 and result == 0:
        print(f'#{x+1} No')
    elif result == 1 and count == 1:
        print(f'#{x+1} Yes')
        