from collections import deque


def f(a):
	q = deque()
	q.append(a)
	visited = [0] * 1000001
	while q:
		x = q.popleft()
		if x == N:
			return visited[x]
		for i in [x*3, x*2, x+1]:
			if i<=N and visited[i] == 0:
				visited[i] = visited[x] + 1
				q.append(i)


N = int(input())
minV = 10000000

print(f(1))