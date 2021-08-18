T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        # 가로확인
        tmp_c = 0
        pc = 0
        while pc <= N-1:
            if arr[i][pc] == 1:
                tmp_c += 1
                pc += 1
            elif arr[i][pc] == 0:
                if tmp_c == K:
                    cnt += 1
                    tmp_c = 0
                else:
                    tmp_c = 0
                pc += 1
            if pc == N:
                if tmp_c == K:
                    cnt += 1

        # 세로확인
        tmp_r = 0
        pr = 0
        while pr <= N - 1:
            if arr[pr][i] == 1:
                tmp_r += 1
                pr += 1
            elif arr[pr][i] == 0:
                if tmp_r == K:
                    cnt += 1
                    tmp_r = 0
                else:
                    tmp_r = 0
                pr += 1
            if pr == N:
                if tmp_r == K:
                    cnt += 1

    print(f'#{tc} {cnt}')