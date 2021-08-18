def check(arr):
    # 가로검증
    for r1 in range(9):
        test = [0] * 10
        for c1 in range(9):
            test[arr[r1][c1]] += 1
        for i in range(1, 10):
            if test[i] != 1:
                return 0
    # 세로 검증
    for c2 in range(9):
        test = [0] * 10
        for r2 in range(9):
            test[arr[r2][c2]] += 1
        for j in range(1, 10):
            if test[j] != 1:
                return 0
    # 3,3 검증
    dr = [0, 3, 6]
    dc = [0, 3, 6]
    for x in dr:
        for y in dc:
            test = [0] * 10
            for a in range(3):
                for b in range(3):
                    test[arr[x+a][y+b]] += 1
            for l in range(1, 10):
                if test[l] != 1:
                    return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {check(arr)}')

