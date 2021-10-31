from collections import deque
import sys
input = sys.stdin.readline

def check(r, c):
	dr = [1, -1, 0, 0]
	dc = [0, 0, -1, 1]
	tmp = 0
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if 0<=nr<R and 0<=nc<C and arr[nr][nc]=='0':
			tmp += 1
			if tmp >= 2:
				return True
	if tmp <= 1:
		return False
def bfs(r, c):
	global minV
	dr = [1, -1, 0, 0]
	dc = [0, 0, -1, 1]
	visited = [[0] * C for _ in range(R)]
	visited[r][c] = 1
	q = deque()
	q.append((r, c))
	while q:
		y, x = q.popleft()
		for i in range(4):
			nr = y + dr[i]
			nc = x + dc[i]
			if 0<=nr<R and 0<=nc<C and visited[nr][nc]==0 and arr[nr][nc] == '0':
				visited[nr][nc] = visited[y][x] + 1
				if minV < visited[nr][nc]:
					return visited[nr][nc]
				if nr == R-1 and nc == C-1:
					return visited[y][x]
				q.append((nr, nc))




R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

minV = 987654321123456789
for r in range(R):
	for c in range(C):
		if arr[r][c] == '1':
			if check(r, c):
				arr[r][c] = '0'
				tmp = bfs(0,0)
				if tmp:
					if tmp < minV:
						minV = tmp
				arr[r][c] = '1'
if minV == 987654321123456789:
	print(-1)
else:
	print(minV+1)
