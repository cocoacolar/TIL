def f(r, c, N, tmp):
	global minV
	if 0<=r<N and 0<=c<N:
		if r == N-1 and c == N-1:
			tmp += arr[r][c]
			if minV > tmp:
				minV = tmp
		else:
			if tmp+arr[r][c] <= minV:
				f(r+1, c, N, tmp+arr[r][c])
				f(r, c+1, N, tmp+arr[r][c])

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	minV = 99999
	tmp = 0
	f(0, 0, N, tmp)
	print(f'#{tc} {minV}')