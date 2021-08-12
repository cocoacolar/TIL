T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_s = 0

    for r in range(N):
        for c in range(N):
            r_count = 0
            c_count = 0
            tmp_s = 0
            if arr[r][c] == 1:
                for i in range(r, N):
                    r_count += 1
                    nr = r + r_count
                    if arr[nr][c]==0 or nr>=N:
                        break
            if arr[r][c] == 1:
                for i in range(r, N):
                    c_count += 1
                    nc = c + c_count
                    if arr[r][nc]==0 or nc>=N:
                        break
            tmp_s = r_count * c_count
            if max_s <tmp_s:
                max_s = tmp_s

    print(f'#{tc} {max_s}')