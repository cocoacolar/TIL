
T = int(input())
for tc in range(1, T+1):
	N, M = map(int, input().split())
	num = list(map(int, input().split()))
	n = 0
	while n < M:
		n+=1
		x = num.pop(0)
		num.append(x)
	print('#{} {}'.format(tc, num[0]))

