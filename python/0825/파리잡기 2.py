T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	pari = [list(map(int, input().split())) for _ in range(N)]
	maxV = 0
	for r in range(N-M+1):
		for c in range(N-M+1):
			tmp = 0
			for x in range(M):
				for y in range(M):
					if x==y or x+y==(M-1):
						tmp += pari[r+x][c+y]
			if tmp> maxV:
				maxV = tmp
	print(f'#{tc} {maxV}')