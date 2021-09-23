T = int(input())

for tc in range(1, T+1):
	N = int(input())
	numbers = [0] + list(map(int, input().split()))
	p = 2
	k = p
	while p < N+1:
		while numbers[k] < numbers[k//2]:
			numbers[k], numbers[k//2] = numbers[k//2], numbers[k]
			k = k//2
		p += 1
		k = p
	t = N//2
	result = 0
	while t >= 1:
		result += numbers[t]
		t = t//2
	print(f'#{tc} {result}')
