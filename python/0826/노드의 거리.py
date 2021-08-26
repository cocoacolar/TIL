def check(arr, S, G):
	visited = [False] * len(arr)
	queue = [arr[S]]
	visited[S] = True
	cnt = 0
	while queue:
		next = queue.pop(0)
		cnt += 1
		tmp = []
		for i in next:
			if i == G:
				return cnt
			if not visited[i]:
				visited[i] = True
				tmp += arr[i]
		if tmp:
			queue.append(tmp)
		else:
			return 0


T = int(input())

for tc in range(1, T+1):
	V, E = map(int, input().split()) # V 노드개수, E 간선수
	arr = [[] for _ in range(V+1)] # 인접리스트

	for i in range(E):
		a, b = map(int, input().split())
		arr[a].append(b)
		arr[b].append(a)
	S, G = map(int, input().split()) # S시작, G 도착

	print('#{} {}'.format(tc, check(arr, S, G)))
