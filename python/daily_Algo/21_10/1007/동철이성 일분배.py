def check(N, k, tmp):
	global result
	if tmp == 0:
		return
	if k == N-1:
		for i in range(N):
			if used[i] == 0:
				tmp *= (arr[k][i]/100)
				if tmp > result:
					result = tmp
				return
	if tmp <= result:
		return
	else:
		for i in range(N):
			if used[i] == 0:
				if (arr[k][i]/100) == 0:
					continue
				used[i] = 1
				tmp *= (arr[k][i]/100)
				check(N, k+1, tmp)
				tmp /= (arr[k][i]/100)
				used[i] = 0

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	result = 0
	used = [0] * N
	tmp = 1
	check(N, 0, tmp)
	result = result*100
	print(f'#{tc} {result:.6f}')