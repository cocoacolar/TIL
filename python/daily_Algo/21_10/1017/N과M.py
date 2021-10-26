def f(M, num, result):

	if M == num:
		for i in result:
			print(i, end=' ')
		print()
	else:
		for i in range(1, N+1):
			if check[i] == 0:
				check[i] = 1
				result.append(arr[i-1])
				f(M, num+1, result)
				result.pop()
				check[i] = 0




N, M = map(int, input().split())

arr = [x for x in range(1, N+1)]
check = [0] * (N+1)
result = []
f(M, 0, result)
