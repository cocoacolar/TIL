# 퀸은 대각선 전체 행 전체 열 전체.......ㅠㅠㅠㅠㅠㅠㅠㅠㅠ하
def check(r, c):
	if r == 0:
		return True
	x1 = c-1
	if x1 >= 0:
		for y in range(r-1, -1, -1):
			if arr[y][x1] == 1:
				return False
			x1 -= 1
			if x1 < 0:
				break
	x2 = c+1
	if x2 < N:
		for y in range(r-1, -1, -1):
			if arr[y][x2] == 1:
				return False
			x2 += 1
			if x2>=N:
				break
	return True

def count_queen(N, r, c):
	global cnt
	if N-1 == r:
		for i in range(N):
			if used[i] == 0:
				if check(r, i):
					cnt += 1
	else:
		for i in range(N):
			if used[i] == 0:
				if check(r, i):
					used[i] = 1
					arr[r][i]  = 1
					count_queen(N, r+1, i)
					arr[r][i] = 0
					used[i] = 0





T = int(input())
for tc in range(1, T+1):
	N = int(input())
	used = [0]*N
	arr = [[0] * N for _ in range(N)]
	cnt = 0
	count_queen(N, 0, 0)
	print(f'#{tc} {cnt}')