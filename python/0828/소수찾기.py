N = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
	cnt = 0
	for i in range(2, num):
		if num%i == 0:
			cnt += 1
			break
	if cnt == 0 and num != 1:
		ans += 1

print(ans)
