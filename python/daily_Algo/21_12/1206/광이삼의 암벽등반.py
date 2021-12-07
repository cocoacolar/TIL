def check(sr, sc, points, N):
	global minV
	global flag
	if minV < N:
		return
	if abs(((R-1)-sr)) + abs(((C-1)-sc)) <= L:
		if minV > N:
			minV = N
			flag = True
		return
	for r, c in points:
		if abs((r-sr))+abs((c-sc)) <= L and visited[r][c] == 0:
			visited[r][c] = 1
			check(r, c, points, N+1)
			visited[r][c] = 0

T = int(input())

for tc in range(1, T+1):
	R, C, L = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(R)]
	arr = arr[::-1]
	visited = [[0] * C for _ in range(R)]
	link = []
	flag = False
	minV = 987654321
	for r in range(R):
		for c in range(C):
			if arr[r][c] == 1:
				link.append((r, c))
	check(0, 0, link, 0)

	if flag:
		print(f'#{tc} {minV}')
	else:
		print(f'#{tc} -1')