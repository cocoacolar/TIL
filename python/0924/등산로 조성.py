from copy import deepcopy

def dfs(r, c, visited):
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	global tmp, max_len
	visited[r][c] = 1
	tmp += 1
	if tmp > max_len:
		max_len = tmp
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if 0 <=nr<N and 0<=nc<N and visited[nr][nc] == 0 and tmp_arr[nr][nc] < tmp_arr[r][c]:
			visited[nr][nc] = 1
			dfs(nr, nc, visited)
			visited[nr][nc] = 0
			tmp -= 1


T = int(input())



for tc in range(1, T+1):
	N, K = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	max_len = 0

	height = []
	tmp_height = 0
	for r in range(N):
		for c in range(N):
			if arr[r][c] > tmp_height:
				tmp_height = arr[r][c]
				height = []
				height.append((r, c))
			elif arr[r][c] == tmp_height:
				height.append((r, c))
	for r, c in height:
		for y in range(N):
			for x in range(N):
				for i in range(K + 1):
					tmp_arr = deepcopy(arr)
					if (r, c) != (y, x):
						tmp_arr[y][x] -= i
						tmp = 0
						visited = [[0]*N for _ in range(N)]
						dfs(r, c, visited)

	print(f'#{tc} {max_len}')