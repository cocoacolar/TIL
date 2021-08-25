
T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x

    h = 0

    maxV = 0
    while h < x//2:
        h += 0.0001
        a = (x - 2 * h) * (y - 2 * h) * h
        if maxV > a:
            break
        if a > maxV:
            maxV = a

    maxV = round(maxV, 7)
    maxV = format(maxV, '6f')
    print('#{} {}'.format(tc, maxV))
