x = int(input())
result = 0
fail = 1
while x >=3:
    if x % 5 == 0:
        result += 5//x
        break

    x -= 3
    if x <3:
        fail = 1
    
    result += 1

if fail:
    print(-1)
else:
    print(result)