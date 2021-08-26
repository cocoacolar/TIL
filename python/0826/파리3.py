def catch(bugs, N, M):
	dr = [[0, 0], [-1, 1], [-1, 1], [1, -1]] #행, 열, 왼쪽대각, 오른쪽 대각
	dc = [[-1, 1], [0, 0], [-1, 1], [-1, 1]]

	maxV = 0
	for r in range(N):
		for c in range(N):
			tmpx = bugs[r][c]
			tmpc = bugs[r][c]
			for a in range(2):
				for b in range(2):
					x, y = r, c
					i, j = r, c
					for k in range(M-1):
						nr = i + dr[a][b]
						nc = j + dc[a][b]
						if 0<= nr < N and 0<= nc < N:
							tmpc += bugs[nr][nc]
							i, j = nr, nc

					for k2 in range(M-1):
						nrx = x + dr[a + 2][b]
						ncx = y + dc[a + 2][b]
						if 0<= nrx < N and 0<= ncx < N:
							tmpx += bugs[nrx][ncx]
							x, y = nrx, ncx

			maxV = max(maxV, tmpc, tmpx)
	return maxV

T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split()) #N 파리칸, M 에프킬라
	bugs = [list(map(int, input().split())) for _ in range(N)]

	print('#{} {}'.format(tc, catch(bugs, N, M)))
