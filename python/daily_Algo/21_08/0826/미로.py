def check(graph):
	for r in range(16):
		for c in range(16):
			if graph[r][c] == '2':
				return int(r), int(c)

def maze(graph, start):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	stack = [start]
	while stack:
		r, c = stack.pop()

		if graph[r][c] == '3':
			return 1
		graph[r][c] = 1
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if 0<= nr < 16 and 0<= nc < 16 and (graph[nr][nc] == '0'or graph[nr][nc] == '3'):

				stack.append((nr, nc))
	return 0


for _ in range(10):
	tc = int(input())
	graph = [list(map(str, input())) for _ in range(16)]

	start = check(graph)
	print('#{} {}'.format(tc, maze(graph, start)))