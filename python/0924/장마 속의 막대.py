
T = int(input())

for tc in range(1, T + 1):
	a, b = map(int, input().split())
	x = b - a
	tmp = x * (x + 1) / 2
	result = tmp - b

	print(f'#{tc} {int(result)}')