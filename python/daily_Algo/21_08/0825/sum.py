T = 10

for tc in range(1,T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(100)]
	maxV = 0
	p1 = 0   #대각
	p2 = 0   #대각2
	for r in range(100):
		tmp = 0
		for c in range(100):
			tmp += arr[r][c]
			if r == c:
				p1 += arr[r][c]
			if r + c == N-1:
				p2 += arr[r][c]

		if tmp > maxV:
			maxV = tmp

	maxV = max(maxV, p1, p2)
	for c in range(100):
		tmp = 0
		for r in range(100):
			tmp += arr[r][c]
		if tmp > maxV:
			maxV = tmp
	print('#{} {}'.format(tc, maxV))
