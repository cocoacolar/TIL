def check(R, C, L):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	direct = [[], [0, 1, 2, 3], [1, 3], [0, 2],[0, 3],[0, 1], [1, 2], [2, 3]]
	stack = [(R, C)]
	time = L-1
	while stack:
		r, c = stack.pop(0)
		for i in direct[arr[r][c]]:
			if i == 0:
				t = 2
			elif i == 1:
				t = 3
			elif i == 2:
				t = 0
			elif i == 3:
				t = 1
			nr = r+dr[i]
			nc = c+dc[i]
			if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
				if t in direct[arr[nr][nc]] and visited[r][c] <= time:
					visited[nr][nc] = visited[r][c] + 1
					stack.append((nr, nc))





T = int(input())

for tc in range(1, T+1):
	N, M, R, C, L = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	visited = [[0]*M for _ in range(N)]
	visited[R][C] = 1
	check(R, C, L)
	ans = 0
	for r in range(N):
		for c in range(M):
			if visited[r][c]:
				ans += 1
	print(f'#{tc} {ans}')
