def f(k):
	dp = [0] * 12
	dp[1], dp[2], dp[3] = 1, 2, 4
	if k == 1:
		return 1
	if k == 2:
		return 2
	if k == 3:
		return 4
	else:
		for i in range(4, k+1):
			dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
		return dp[k]

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	print(f(N))

