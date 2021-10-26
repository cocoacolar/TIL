N = int(input())
arr = []
for i in range(N):
	height, weight = map(int, input().split())
	arr.append([height, weight, i])

arr.sort(key=lambda x:(x[0], x[1]), reverse=True)
arr = [[10000, 10000, -999]] + arr
rank = 0
tmp = 0


for k in range(1, N+1):
	if arr[k-1][0] > arr[k][0] and arr[k-1][1] > arr[k][1]:
		rank += tmp
		tmp = 0
		rank += 1
		arr[k].append(rank)
	else:
		arr[k].append(rank)
		tmp += 1

arr.sort(key=lambda x:x[2])

for j in range(1, N+1):
	print(arr[j][3], end=' ')
