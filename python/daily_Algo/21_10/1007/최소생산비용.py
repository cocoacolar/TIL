def check(N, k, tmp):
	global result

	if k == N-1:
		for i in range(N):
			if used[i] == 0:
				tmp += arr[k][i]
		if tmp < result:
			result = tmp
		return
	if tmp >= result:
		return
	else:
		for i in range(N):
			if used[i] == 0:
				used[i] = 1
				tmp += arr[k][i]
				check(N, k+1, tmp)
				used[i] = 0
				tmp -= arr[k][i]

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	result = 1000001
	tmp = 0
	used = [0]*N
	check(N, 0, tmp)
	print(f'#{tc} {result}')

