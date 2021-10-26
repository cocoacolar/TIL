#탐색 DFS 만들기
def dfs(arr, M, N):
    graph = [[False] * M for _ in range(N)]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1] # 시계방향으로 이동
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0: # 땅이 아니면 찾지않음
                continue
            if arr[r][c] == 1 and graph[r][c] == True: # 땅이지만 이미 탐색한 곳이라면 패스
                continue
            if arr[r][c] == 1 and graph[r][c]== False:
                count += 1
                graph[r][c] = True
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for i in range(8):
                        nx = x + dr[i]
                        ny = y + dc[i]
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1 and graph[nx][ny]==False:
                            graph[nx][ny] = True
                            stack.append((nx, ny))
    return count



while True:
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    if M == 0 and N == 0:
        break
    else:
        print(dfs(arr, M, N))
