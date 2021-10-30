from collections import deque

import sys
input = sys.stdin.readline

def bfs(k):
	visited[k] = 1
	q = deque()
	q.append(k)
	while q:
		x = q.popleft()
		for i in adjL[x]:
			if visited[i] == 0:
				visited[i] = 1
				q.append(i)

N, M = map(int, input().split())


adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
	a, b = map(int, input().split())
	adjL[a].append(b)
	adjL[b].append(a)
result = 0
for k in range(1, N+1):
	if visited[k]==0:
		result += 1
		bfs(k)
print(result)