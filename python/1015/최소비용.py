from collections import deque

def check(r, c, N):
	dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
	visited[r][c] = 0
	q = deque()
	q.append((r,c))

	while q:
		y, x = q.popleft()
		for i in range(4):
			nr = y + dr[i]
			nc = x + dc[i]

			if 0<=nr<N and 0<=nc<N:
				cost = visited[y][x]+1
				if arr[y][x] < arr[nr][nc]:
					cost += (arr[nr][nc]-arr[y][x])
				if cost < visited[nr][nc]:
					visited[nr][nc] = cost
					q.append((nr, nc))


	return visited[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	visited = [[99999999999]*N for _ in range(N)]

	print(check(0,0,N))