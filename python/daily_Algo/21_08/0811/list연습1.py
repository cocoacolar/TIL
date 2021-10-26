T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1] # 우하좌상
    dc = [1, 0, -1, 0]
    result = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0<=nr<N and 0<=nc<N:
                    result += abs(arr[r][c]-arr[nr][nc])

    print(f'#{tc} {result}')