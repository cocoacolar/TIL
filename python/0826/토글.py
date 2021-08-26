T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	graph = [[0]+list(map(int, input().split())) for _ in range(N)]
	graph = [[0] * (N+1)] + graph

	k = 1
	while k <= M:

		for r in range(1, N+1):
			for c in range(1, N+1):
				if M%k == 0 or k == M:
					graph[r][c] = (graph[r][c]+1) % 2
					continue
				if r+c == k or (r+c)%k == 0:
					graph[r][c] = (graph[r][c]+1) % 2
		k += 1

	cnt = 0
	for i in range(1, N+1):
		for j in range(1, N+1):
			cnt += graph[i][j]


	print('#{} {}'.format(tc, cnt))