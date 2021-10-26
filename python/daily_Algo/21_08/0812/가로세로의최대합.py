T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max_s = 0
    for r in range(N):
        for c in range(N):
            tmp_s =0
            for i in range(N):
                tmp_s += (arr[r][i] + arr[i][c])
            tmp_s -= arr[r][c]

            if tmp_s > max_s:
                max_s = tmp_s

    print(f'#{tc} {max_s}')
