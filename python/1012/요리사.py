from itertools import combinations
T = int(input())

for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]

	num = [i for i in range(N)]

	result = []
	numA_lst = list(combinations(num, N//2))
	ans = 9999999
	for k in range(len(numA_lst)//2):
		used = [0] * N
		numB = []
		numA = list(numA_lst[k])
		for x in numA:
			used[x] = 1
		for i in range(N):
			if used[i] == 0:
				numB.append(i)
		A = 0
		B = 0
		for i in range(len(numA)):
			for j in range(len(numA)):
				if i != j:
					A += arr[numA[i]][numA[j]]
		for i in range(len(numB)):
			for j in range(len(numB)):
				if i != j:
					B += arr[numB[i]][numB[j]]

		result = abs(A-B)

		ans = min(result, ans)

	print(f'#{tc} {ans}')