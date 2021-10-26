def tile(N):
	dp = [0] * (N+1)
	if N==1:
		print(1)
		return
	if N==2:
		print(2)
		return
	else:
		dp[1] = 1
		dp[2] = 2
		for i in range(3, N+1):
			dp[i] = (dp[i-1] + dp[i-2])%15746
		print(dp[N])
		return

N = int(input())
tile(N)