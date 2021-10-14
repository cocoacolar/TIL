from collections import deque

def check(N, M):
	visited = [0] * (1000000+1)
	visited[N] = 1
	q = deque()
	q.append(N)
	while q:
		x = q.popleft()
		for ans in [x*2, x+1, x-1, x-10]:
			if ans == M:

				return visited[x]
			if 1<= ans <=1000000 and visited[ans]==0:
				visited[ans] = visited[x]+1
				q.append(ans)

T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	result = check(N, M)
	print(f'#{tc} {result}')
