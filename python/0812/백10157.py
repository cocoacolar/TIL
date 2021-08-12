M, N = map(int, input().split()) #N행 M열
K = int(input())
S = [[False]*M for _ in range(N)]

dr = [1, 0, -1, 0] # 상 우 하 좌
dc = [0, 1, 0, -1]
num = 1
r = -1
c = 0
p = 0
flag = False
if K > M*N:
    print(0)
else:
    while num <= M*N+1:
        if flag:
            print(f'{c+1} {r+1}')
            break
        nr = r + dr[p]
        nc = c + dc[p]
        if 0<=nr<N and 0<=nc<M and S[nr][nc] == False:
            r, c = nr, nc
            S[nr][nc] = num

            if num == K:
                flag = True
            num += 1
        else:
            p = (p+1)%4
