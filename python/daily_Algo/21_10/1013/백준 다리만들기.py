#땅 종류 변경
def dfs(r, c, N, num):
	if r<0 or r>=N or c<0 or c>=N or visited[r][c]==1 or arr[r][c]==0:
		return
	visited[r][c] = 1
	arr[r][c] = num
	dfs(r+1, c, N, num)
	dfs(r-1, c, N, num)
	dfs(r, c+1, N, num)
	dfs(r, c-1, N, num)

# 최소다리 체크
def check_x(r, c, N):
	# 가로 체크
	dr = [-1, 0, 1]
	dc = [0, 1, 0]
	x = arr[r][c]
	p = 1
	c += 1
	while c < N-1:
		if arr[r][c] == x:
			return False
		elif arr[r][c] == 0:
			for i in range(3):
				nr = r + dr[i]
				nc = c + dc[i]
				if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=0 and arr[nr][nc]!=x:
					p+=1
					return p
			p += 1
			c += 1
	return False

def check_y(r, c, N):
	# 세로 체크
	dr = [0, 1, 0]
	dc = [-1, 0, 1]
	x = arr[r][c]
	p = 1
	r += 1
	while r < N-1:
		if arr[r][c] == x:
			return False
		elif arr[r][c] == 0:
			for i in range(3):
				nr = r + dr[i]
				nc = c + dc[i]
				if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=0 and arr[nr][nc]!=x:
					p += 1
					return p
			p += 1
			r += 1
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
result = 999999
for r in range(N):
	for c in range(N):
		if arr[r][c] != 0:
			re1 = check_x(r, c, N)
			re2 = check_y(r, c, N)
			if re1:
				result = min(re1, result)
			if re2:
				result = min(re2, result)
print(result-1)
