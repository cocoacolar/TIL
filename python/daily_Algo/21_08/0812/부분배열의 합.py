T = int(input())

for tc in range(1, T+1):
    N, n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    rlt_m = 0
    for mr in range(N):
        for mc in range(N):
            n_r = mr + n
            n_c = mc + m
            tmp_m = 0
            if 0<=n_r<=N and 0<=n_c<=N:
                for i in range(mr, n_r):
                    for j in range(mc, n_c):
                        tmp_m += arr[i][j]

                if rlt_m < tmp_m:
                    rlt_m = tmp_m

    print(f'#{tc} {rlt_m}')