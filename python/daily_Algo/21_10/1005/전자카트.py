def f(r, c, tmp, check):
	global minV
	if sum(check) == N:
		tmp += arr[r][c]
		tmp += arr[c][0]
		if minV > tmp:
			minV = tmp
	else:
		for i in range(N):
			if c != i and check[i] == 0:
				check[i] = 1
				f(c, i, tmp+arr[r][c], check)
				check[i] = 0




T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	check = [0] * N
	check[0] = 1
	minV = 99999
	tmp = 0
	f(0, 0, tmp, check)
	print(f'#{tc} {minV}')