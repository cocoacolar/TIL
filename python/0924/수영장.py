

T = int(input())

for tc in range(1, T+1):
	cost = list(map(int, input().split()))
	arr = [0, 0, 0] + list(map(int, input().split()))
	tmp = [0] * 15
	for i in range(3, 15):
		if arr[i]:
			x = cost[0] * arr[i] + tmp[i-1]
			y = cost[1] + tmp[i-1]
			z = cost[2] + tmp[i-3]
			min_C = min(x, y, z)
			tmp[i] = min_C
		else:
			tmp[i] = tmp[i-1]

	result = min(tmp[14], cost[3])

	print(f'#{tc} {result}')
