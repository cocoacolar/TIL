T = 10

for tc in range(1, T+1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    tem = 0
    for r in range(100):  # 행의 합
        for c in range(100):
            tem += arr[r][c]
        if tem > result:
            result = tem
            tem = 0
        else:
            tem = 0

    for c in range(100):  # 열의 합
        for r in range(100):
            tem += arr[r][c]
        if tem > result:
            result = tem
            tem = 0
        else:
            tem = 0

    r = 0  # 대각선 합
    c = 0
    tem = 0
    while r <= 99:
        tem += arr[r][c]
        r += 1
        c += 1
    if tem > result:
        result = tem
        tem = 0
    else:
        tem = 0

    r = 0
    c = 99
    tem = 0

    while r <= 99:
        tem += arr[r][c]
        r += 1
        c -= 1
    if tem > result:
        result = tem
        tem = 0
    else:
        tem = 0

    print(f'#{tc} {result}')