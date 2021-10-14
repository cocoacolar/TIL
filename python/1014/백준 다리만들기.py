#땅 종류 변경
def dfs(r, c, N, num):
	dr = [1, -1, 0, 0]
	dc = [0, 0, 1, -1]
	stack = [(r,c)]
	while stack:
		y, x = stack.pop()
		visited[y][x] = 1
		arr[y][x] = num
		for i in range(4):
			nr = y + dr[i]
			nc = x + dc[i]
			if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and arr[nr][nc]==1:
				stack.append((nr, nc))
# 최소다리 체크
# 여기서 주의할 점은 BFS 방문 체크시 q에 집어 넣을때 방문 체크를해야 중복방문이 이루어지지 않는다.
# 이전에 체크를 하면 중복 방문이 발생하여 메모리 초과가 발생한다
def bfs(r, c, N):
	global result
	check = [[0] * N for _ in range(N)]
	check[r][c] = 1
	tmp = 0
	key = arr[r][c]
	dr = [1, -1, 0, 0]
	dc = [0, 0, 1, -1]
	q = [[(r, c)]]
	while q:
		lst = q.pop(0)
		step = []
		for y, x in lst:
			if arr[y][x] != key and arr[y][x]!=0:
				return tmp

			for i in range(4):
				nr = y + dr[i]
				nc = x + dc[i]
				if 0 <= nr < N and 0 <= nc < N and check[nr][nc] == 0 and arr[nr][nc] !=key:
					check[nr][nc] = 1
					step.append((nr,nc))
		if step:
			q.append(step)

		tmp += 1
		if tmp > result:
			return False
	return False






N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 배열 변경
num = 1
for r in range(N):
	for c in range(N):
		if arr[r][c]==1 and visited[r][c]==0:
			dfs(r, c, N, num)
			num += 1
visited = 0
result = 999999
for r in range(N):
	for c in range(N):
		if arr[r][c] != 0:
			k = bfs(r, c, N)
			if k:
				result = min(result, k)

print(result-1)
