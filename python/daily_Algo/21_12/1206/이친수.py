N = int(input())
dp = [0] * (91)

for i in range(N+1):
	if i == 1:
		dp[1] = 1
	elif i == 2:
		dp[2] = 1
	elif i == 3:
		dp[3] = 2
	elif i == 4:
		dp[4] = 3
	else:
		dp[i] = sum(dp[1:i-1])+1

print(dp[N])


