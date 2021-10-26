T = int(input())
for tc in range(1, T+1):
    N = int(input())

    x = [[False] * N for _ in range(N)]

    count = 1
    dr = [0, 1, -0, -1] #동 남 서 북
    dc = [1, 0, -1,  0]
    r = 0
    c = -1
    k = 0
    while count <= N*N:
        nr = r + dr[k]
        nc = c + dc[k]
        if  0<=nr<N and  0<=nc<N and x[nr][nc] == False:
            x[nr][nc] = count
            count += 1
            r, c = nr, nc
        else:
            k = (k+1)%4


    print(f'#{tc}')
    for k in x:
        for p in k:
            print(p, end=' ')
        print()