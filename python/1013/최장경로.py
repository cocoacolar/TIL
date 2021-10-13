def check(i, tmp):
	global result
	visited[i] = 1
	if tmp > result:
		result = tmp
	for a in adjL[i]:
		if visited[a] == 0:
			check(a, tmp+1)
	visited[i] = 0


T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split()) #N정점, M 노드수
	adjL = [[] for _ in range(N+1)]
	visited = [0] * (N + 1)
	for _ in range(M):
		x, y = map(int, input().split())
		adjL[x].append(y)
		adjL[y].append(x)

	result = 0
	for i in range(1, N+1):
		tmp = 1
		check(i, tmp)
	print(f'#{tc} {result}')