T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]

	big = 0
	for r in range(N-M+1):
		for c in range(N-M+1):
			tmp = 0
			for x in range(M):
				for y in range(M):
					tmp += arr[x+r][y+c]
			if tmp>big:
				big = tmp

	print('#{} {}'.format(tc, big))