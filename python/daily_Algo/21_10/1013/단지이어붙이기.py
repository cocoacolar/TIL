def dfs(arr, N):
	visited = [[False] * N for _ in range(N)]
	dr = [0, 1, 0, -1]  # 우, 하 , 좌, 상
	dc = [1, 0, -1, 0]
	total = 0
	result = []
	for r in range(N):
		for c in range(N):
			if arr[r][c] == 1 and visited[r][c] == False:
				total += 1
				stack = [(r, c)]
				cnt = 0
				visited[r][c] = True
				while stack:
					cnt += 1
					x, y = stack.pop()
					for i in range(4):
						nr = x + dr[i]
						nc = y + dc[i]
						if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and arr[nr][nc] == 1:
							visited[nr][nc] = True
							stack.append((nr, nc))
				result.append(cnt)
	return (total, result)

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
a, b = dfs(arr, N)
print(a)
b.sort()
for i in b:
	print(i)