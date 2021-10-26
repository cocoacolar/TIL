def check(r, c, tmp):

	if 0<=r<N and 0<=c<N and (arr[r][c] not in tmp):
		return 1
	else:
		return 0

def left(r, c, sr, sc, sp, tmpL, loc, loc_n):
	global result

	dr = [1, -1, -1, 1]
	dc = [1, 1, -1, -1]
	nr = r + dr[sp]
	nc = c + dc[sp]
	if loc[0] < loc[2] or loc[1] < loc[3]:
		return
	if nr == sr and nc == sc:
		result = max(result, len(tmpL))

		return True
	if check(nr, nc, tmpL):
		tmpL.append(arr[nr][nc])
		for i in range(2):
			if i == 1:
				loc[loc_n] += 1
				left(nr, nc, sr, sc, (sp + i) % 4, tmpL, loc, (loc_n+1)%4)
				loc[loc_n] -= 1

			else:
				loc[loc_n] += 1
				left(nr, nc, sr, sc, (sp + i) % 4, tmpL, loc, loc_n)
				loc[loc_n] -= 1

		tmpL.pop()


T = int(input())
for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	# 시작 위치 찾기
	result = 0
	for r in range(1, N-1):
		for c in range(N-2): # 값 비교하기
			loc=[0, 0, 0, 0]
			tmpL = [arr[r][c]]
			loc_n = 0
			a = 0
			left(r, c, r, c, a, tmpL, loc, loc_n)


	if result:
		print(f'#{tc} {result}')
	else:
		print(f'#{tc} -1')
