
T = int(input())
for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr = list(map(int, input().split()))
	for i in range(N):
		arr[i] = (arr[i], i)
	ans = 1
	while True:
		num, idx = arr.pop(0)
		flag = False
		for x, y in arr:
			if num < x:
				arr.append((num, idx))
				flag = True
				break
		if not flag:
			if idx == M:
				break
			else:
				ans += 1
	print(ans)