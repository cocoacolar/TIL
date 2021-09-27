def dfs(i, visited, adj):
	stack = [i]
	while stack:
		x = stack.pop()
		for a in adj[x]:
			if visited[a] == 0:
				visited[a] = 1
				stack.append(a)
				print(visited)


def solution(n, computers):
	visited = [0] * n
	R = len(computers)
	C = len(computers[0])
	adj = {}
	for r in range(R):
		for c in range(r, C):
			if computers[r][c] == 1:
				if adj.get(r, -1) == -1:
					adj[r] = [c]
				else:
					adj[r].append(c)

	print(adj)
	answer = 0
	for i in range(n):
		if visited[i] == 0:
			answer += 1
			visited[i] = 1
			dfs(i, visited, adj)

	return answer

a = 5

computers = [
	[1, 1, 0, 1, 0],
	[1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1],
	[1, 0, 1, 1, 0],
	[0, 0, 1, 0, 1]
]

print(solution(a, computers))
