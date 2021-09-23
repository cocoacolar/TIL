T = int(input())

for tc in range(1, T+1):
	N, M, L = map(int, input().split())
	num = [0] * (N+1)
	for i in range(M):
		x, y = map(int, input().split())
		num[x] = y

	for k in range(N, -1, -1):
		t = k//2
		num[t] += num[k]

	print(f'#{tc} {num[L]}')

