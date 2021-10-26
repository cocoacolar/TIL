def di(N):
	start = 0
	minV = INF
	for i in range(N+1):
		if dist[0][i] !=INF and minV>dist[0][i]:
			minV = dist[0][i]
			start = i
	tmp = minV
	visited = [0]*(N+1)
	visited[0], visited[start] = 1, 1

	while start != N:
		# 그 다음 방문해서 연결된곳 들의 값을 dist값과 비교하여 변경
		for i in range(N+1):
			if adjM[start][i] != 0:
				k = tmp + adjM[start][i]
				if k < dist[0][i]:
					dist[0][i] = k
		# 이미 방문한 곳 이외에 그 다음 최소 방문값 결정
		minV = INF
		for p in range(N+1):
			if visited[p] == 0 and dist[0][p] < minV:
				start = p

				minV = dist[0][p]
		tmp = minV
		visited[start] = 1

	return tmp


T = int(input())

for tc in range(1, T+1):
	N, E = map(int, input().split())
	INF = 987654321
	adjM = [[0] * (N+1) for _ in range(N+1)]
	dist = [[INF] * (N + 1) for _ in range(N + 1)]
	for _ in range(E):
		a, b, w = map(int, input().split())
		adjM[a][b] = w
		dist[a][b] = w

	print(f'#{tc} {di(N)}')