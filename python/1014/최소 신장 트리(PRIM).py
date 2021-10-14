def check(start, V, E):  #prim 1방식 최소 비용 찾아 key값으로 찾기

	n = V
	MST[0] = 1
	while n>0:  #여기서 for문 돌려도 된다.
		u = 0
		minV = 10000
		for i in range(V + 1):
			if MST[i] == 0 and key[i] < minV:
				u = i
				minV = key[i]
		MST[u] = 1
		for v in range(V+1):
			if MST[v]== 0 and adjM[u][v]>0:
				key[v] = min(key[v], adjM[u][v])
		n -= 1
	return sum(key)


T = int(input())

for tc in range(1, T+1):
	V, E = map(int, input().split())
	adjM = [[0] * (V+1) for _ in range(V+1)]
	for _ in range(E):
		r, c, w = map(int, input().split())
		adjM[r][c] = w
		adjM[c][r] = w

	MST = [0]*(V+1)
	key = [99999]*(V+1)
	key[0] = 0
	print(f'#{tc} {check(0, V, E)}')