T = 10
def check(x):
	if num[x].isdigit():
		return int(num[x])
	elif num[x] == '+':
		result = check(adj[x][0]) + check(adj[x][1])
		return result
	elif num[x] == '-':
		result = check(adj[x][0]) - check(adj[x][1])
		return result
	elif num[x] == '*':
		result = check(adj[x][0]) * check(adj[x][1])
		return result
	elif num[x] == '/':
		result = check(adj[x][0]) / check(adj[x][1])
		return result

for tc in range(1, T+1):
	N = int(input())
	num = [False] * (N+1)
	adj = [False] * (N+1)
	for i in range(N):
		arr = list(map(str, input().split()))
		num[int(arr[0])] = arr[1]
		if len(arr) == 4:
			adj[int(arr[0])] = [int(arr[2]), int(arr[3])]

	print(f'#{tc} {int(check(1))}')

