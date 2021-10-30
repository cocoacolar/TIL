N = int(input())

dp = [0] * (N+2)

dp[1] = 1
dp[2] = 2

p = 3
while p <= N:
	dp[p] = (dp[p-1] + dp[p-2])%10007
	p += 1
print(dp[N])
