from collections import deque

def check(N, M):
	q.append(N)
	global minV
	visited[N] = 1
	while q:
		x = q.popleft()
		for i in [x-1, x+1, x*2]:
			if i == M:
				minV = min(minV, visited[x])
				return
			if 0<=i<=100000 and visited[i] == 0:
				visited[i] = visited[x]+1
				q.append(i)

N, M = map(int, input().split())
visited = [0] * 100001
q = deque()
minV = 99999999
if N == M:
	print(0)
else:
	check(N, M)
	print(minV)