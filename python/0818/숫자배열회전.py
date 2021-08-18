import copy

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr1 = copy.deepcopy(arr)   #90
    arr2 = copy.deepcopy(arr)   #180
    arr3 = copy.deepcopy(arr)   #270

    # 90도 전환
    for r1 in range(N):
        for c1 in range(N):
            if r1 < c1:
                arr1[r1][c1], arr1[c1][r1] = arr1[c1][r1], arr1[r1][c1]
    for i in range(N):
        arr1[i] = arr1[i][::-1]
    for j in range(N):
        word = ''
        for k in range(N):
            word += arr1[j][k]
        arr1[j] = word

    # 180 전환
    for p in range(N):
        arr2[p] = arr2[p][::-1]
    for l in range(int(N/2)):
        arr2[l], arr2[N-1-l] = arr2[N-1-l], arr2[l]
    for a in range(N):
        word2 = ''
        for b in range(N):
            word2 += arr2[a][b]
        arr2[a] = word2


    # 270 전환
    for r1 in range(N):
        for c1 in range(N):
            if r1 < c1:
                arr3[r1][c1], arr3[c1][r1] = arr3[c1][r1], arr3[r1][c1]
    for l in range(int(N/2)):
        arr3[l], arr3[N-1-l] = arr3[N-1-l], arr3[l]

    for x in range(N):
        word3 = ''
        for y in range(N):
            word3 += arr3[x][y]
        arr3[x] = word3
    print(f'#{tc}')
    for i in range(N):
        print(arr1[i], end=' ')
        print(arr2[i], end=' ')
        print(arr3[i])