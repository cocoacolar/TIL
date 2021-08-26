def check(maze, S):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	queue = [[S]]
	cnt = -1
	while queue:
		cnt += 1
		tmp = []
		i = queue.pop(0)
		for r, c in i:
			x, y = r, c
			for i in range(4):
				nr = x + dr[i]
				nc = y + dc[i]
				if 0<=nr<N and 0<=nc<N and maze[nr][nc]==3:

					return cnt
				if 0<=nr<N and 0<=nc<N and maze[nr][nc]==0:
					maze[nr][nc] = 1
					tmp += [(nr, nc)]
		if tmp:
			queue.append(tmp)
		else:
			return 0
T = int(input())

for tc in range(1, T+1):
	N = int(input())
	maze = [list(map(int, input())) for _ in range(N)]

	S = 0

	for r in range(N):
		for c in range(N):
			if maze[r][c] == 2:
				S = (r, c)
	print('#{} {}'.format(tc, check(maze, S)))