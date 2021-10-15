from collections import deque


def check(start):
	group[start] = 1
	q = deque()
	q.append(start)

	while q:
		x = q.popleft()
		for i in adjL[x]:
			if group[i] == 0:
				group[i] = 1
				q.append(i)


T = int(input())

for tc in range(1, T+1):
	N, M  = map(int, input().split())
	adjL = [[] for _ in range(N+1)]
	group = [0] * (N+1)
	for _ in range(M):
		x, y = map(int, input().split())
		adjL[x].append(y)
		adjL[y].append(x)
	tmp = 0
	for i in range(1, N+1):
		if group[i] == 0:
			tmp += 1
			check(i)
	print(f'#{tc} {tmp}')