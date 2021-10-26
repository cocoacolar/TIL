T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N) for _ in range(N)]

    # 파스칼 삼각형 만들기
    for r in range(N):
        for c in range(r+1):
            if (r == c) or c == 0:
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r-1][c]+arr[r-1][c-1]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()
