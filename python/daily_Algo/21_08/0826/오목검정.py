def check(table, N):
	dr = [0, 1, 1, 1] 
	dc = [1, 0, 1, -1]
	for r in range(N):
		for c in range(N):
			if table[r][c] == 'o':
				for j in range(4):
					cnt = 1
					nr = r+dr[j]
					nc = c+dc[j]
					while True:
						if 0<= nr< N and 0<=nc<N and table[nr][nc] == 'o':
							cnt += 1
							nr += dr[j]
							nc += dc[j]
						else:
							break
					if cnt == 5:
						return 'YES'
	return 'NO'

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	table = [list(input()) for _ in range(N)]

	print('#{} {}'.format(tc, check(table, N)))