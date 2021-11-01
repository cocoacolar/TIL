from itertools import combinations

def check():
	if arr[-1] == N:
		return 1
	else:
		for num in range(2, 4):
			k = list(combinations(arr, num))
			for i in k:
				if sum(i) == N:
					return num
		return 4



N = int(input())
arr = []
for i in range(1, N):
	if i**2 > N:
		break
	else:
		arr.append(i**2)
print(check())
