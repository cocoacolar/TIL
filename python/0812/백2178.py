from collections import deque

M, N = map(int, input().split())
arr=[]
for i in range(M):
    arr.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nc <=-1 or nc >= N or nr <= -1 or nr >= M:
                continue
            if arr[nr][nc] == 0:
                continue
            if arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))
        
    return arr[M-1][N-1] 
print(bfs(0, 0))

