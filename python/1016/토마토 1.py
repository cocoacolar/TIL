from collections import deque
import sys
input = sys.stdin.readline

def check(R, C):
	dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]
	while q:

		y, x = q.popleft()
		for i in range(4):
			nr = y + dr[i]
			nc = x + dc[i]
			if 0<=nr<R and 0<=nc<C and arr[nr][nc]==0:
				arr[nr][nc] = arr[y][x] + 1
				q.append((nr, nc))



C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
q = deque()
for r in range(R):
	for c in range(C):
		if arr[r][c] == 1:
			q.append((r, c))

check(R, C)
flag = False
maxV = -1
for r in range(R):
	for c in range(C):
		if arr[r][c] == 0:
			flag = True
			break
		else:
			maxV = max(maxV, arr[r][c])
	if flag:
		break
if flag:
	print(-1)
elif maxV == 1:
	print(0)
else:
	print(maxV-1)