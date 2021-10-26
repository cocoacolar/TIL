def find(x, N, cnt):
	global result

	if N <= x:
		if cnt < result:
			result = cnt
		return
	if cnt >= result:
		return
	else:
		for i in range(1, arr[x]+1):
			cnt += 1
			find(x+i, N, cnt)
			cnt -= 1

T = int(input())

for tc in range(1, T+1):
	arr = list(map(int, input().split()))
	N = arr[0]

	result = 100001
	cnt = -1
	find(1, N, cnt)

	print(f'#{tc} {result}')





