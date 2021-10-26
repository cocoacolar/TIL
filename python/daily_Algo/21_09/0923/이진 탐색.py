def inorder(n, V):
	global cnt
	if n <= V:
		inorder(n * 2, V)
		cnt += 1
		num[n] = cnt
		inorder(n * 2 + 1, V)

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	num = [0] * (N + 1)
	cnt = 0
	inorder(1, N)
	print(f'#{tc} {num[1]} {num[N//2]}')