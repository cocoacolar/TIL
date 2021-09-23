from collections import deque

T = int(input())

def check(N, M, queue):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nr = x + dr[i]
			nc = y + dc[i]
			if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 'L':
				visited[nr][nc] = visited[x][y] + 1
				queue.append((nr, nc))

for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr = [input() for _ in range(N)]
	visited = [[0] * M for _ in range(N)]
	ans = 0
	queue = deque()
	for r in range(N):
		for c in range(M):
			if arr[r][c] == 'W':
				queue.append((r, c))
	check(N, M, queue)
	for r in range(N):
		for c in range(M):
			ans += visited[r][c]

	print(f'#{tc} {ans}')
