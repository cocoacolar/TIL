T = int(input())

for tc in range(1, T+1):
	N = int(input())
	card = list(map(str, input().split()))
	if N%2 == 0:
		A = card[:(N//2)+1]
		B = card[(N//2):]
	else:
		A = card[:(N // 2) + 1]
		B = card[(N // 2)+1:]
	i = 0
	ap = 0
	bp = 0
	print('#{}'.format(tc), end=' ')
	while i != N:

		if i % 2 == 0:
			print(A[ap], end=' ')
			ap += 1
		else:
			print(B[bp], end=' ')
			bp += 1
		i += 1

	print()