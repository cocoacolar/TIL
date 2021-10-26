from collections import deque

T = int(input())
N = int(input())
visited = [False]*(T+1)
graph = [[] for _ in range(T+1)]


# 그래프 만들기
for i in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# bfs 그래프 탐색
def bfs(graph, start, visited):
    que = deque([start])

    while que:
        x = que.popleft()
        visited[x] = True
        for k in graph[x]:
            if visited[k] == False:
                que.append(k)

    return visited.count(True)

print(bfs(graph,  1, visited)-1)
