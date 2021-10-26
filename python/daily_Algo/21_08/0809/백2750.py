def quick(x):
    left, right = 1, len(x)-1
    if len(x)%2:
        while left <right:
            if x[left] > x[right]:
                x[left],  x[right] = x[left],  x[right]
            left += 1
            right += 1
        x[0], x[left] = x[left], x[0]
    else:
        while left <right:
            if x[left] > x[right]:
                x[left],  x[right] = x[left],  x[right]
            left += 1
            right += 1
        x[0], x[left] = x[left], x[0]

T = int(input())
tem = []
for i in range(T):
    a = int(input())
    tem.append(a)



