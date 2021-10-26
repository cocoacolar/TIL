N = int(input())
arr = []
for i in range(N):
	x, y = map(int, input().split())
	arr.append((x, y, i))

arr.sort(key=lambda x:(x[0], x[1]), reverse=True)

result = [0] * N
arr = [(0, 0, N)] + arr
n = 1
k = 1
for j in range(1, N+1):
	if j == 1:
		result[arr[j][2]] = n
		continue
	if arr[j-1][0] > arr[j][0] and arr[j-1][1] > arr[j][1]:
		n = n + k
		result[arr[j][2]] = n
		k = 1
	else:
		result[arr[j][2]] = n
		k += 1

for i in result:
	print(i, end=' ')