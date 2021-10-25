def change(N):
	result = [[0] * (2*N) for _ in range(2*N)]
	for r in range(2*N):
		for c in range(2*N):
			if 0<=r<N and 0<=c<N: # A영역
				result[r][c] = arr[r][c]

			if 0<= r <N and N<=c<(2*N): # B영역
				result[r][c] = result[r][(2*N)-1-c]

			if N<=r<(2*N) and 0<= c <N: # C영역
				result[r][c] = result[(2*N)-1-r][c]

			if N<=r<(2*N) and N<=c<(2*N): #D영역
				result[r][c] = arr[(2*N)-1-c][(2*N)-1-r]
	return result

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]

	# 정답 출력
	print(f'#{tc}')
	ans = change(N)
	for r in range(2*N):
		for c in range(2*N):
			print(ans[r][c], end=' ')
		print()