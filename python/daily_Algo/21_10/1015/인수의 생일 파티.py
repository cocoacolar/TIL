from collections import deque

def di(X, arr):
	dist = [INF] * (N+1)
	dist[X] = 0
	q = deque()
	q.append(X)
	while q:
		n = q.popleft()
		for node, cost in arr[n]:
			k = dist[n] + cost
			if dist[node] > k:
				dist[node] = k
				q.append(node)

	return dist[1:]




T = int(input())
INF = 987654321
for tc in range(1, T+1):
	N, M, X = map(int, input().split())
	come = [[] for _ in range(N+1)]
	back = [[] for _ in range(N+1)]

	for _ in range(M):
		x, y, w = map(int, input().split())
		come[x].append((y, w))
		back[y].append((x, w))

	A = di(X, come)
	B = di(X, back)
	ans = 0
	for i in range(N):
		t = A[i] + B[i]
		if t > ans:
			ans = t
	print(f'#{tc} {ans}')
