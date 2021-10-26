def dfs(R, C, r, c, arr, visited):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	stack = [(r,c)]
	while stack:
		r, c = stack.pop()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if 0<=nr<R and 0<=nc<C and arr[nr][nc] == 1 and visited[nr][nc] == 0:
				visited[nr][nc] = 1
				stack.append((nr, nc))


T = int(input())

for tc in range(1, T+1):
	C, R, K = map(int, input().split())
	arr = [[0] * C for _ in range(R)]
	visited = [[0] * C for _ in range(R)]
	cnt = 0
	for i in range(K):
		c, r = map(int, input().split())
		arr[r][c] = 1

	for r in range(R):
		for c in range(C):
			if arr[r][c] == 1 and visited[r][c] == 0:
				cnt += 1
				visited[r][c] = 1
				dfs(R, C, r, c, arr, visited)
	print(cnt)