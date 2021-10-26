def check(num, N):
	k = 0
	for pole in arr:
		if num <= pole:
			k += pole//num
		if k >= N:
			return True
	return False


def binary_search():
	start = 1
	end = (arr[-1]+1)
	while (end-start)>1:
		mid = (start + end)//2
		if check(mid, N):
			start = mid
		else:
			end = mid

	return start

K, N = map(int, input().split())
arr = []
for _ in range(K):
	arr.append(int(input()))
arr.sort()
print(binary_search())
