
T=int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    max_s = 0
    for r in range(M):
        for c in range(M):
            n_r = r+N
            n_c = c+N
            tem_s = 0
            if 0<=n_c<=M and 0<=n_r<= M:
                for i in range(r, n_r):
                    for j in range(c, n_c):
                        tem_s += arr[i][j]

                if max_s < tem_s:
                    max_s = tem_s



    print(f'#{tc} {max_s}')