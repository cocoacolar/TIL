def dfs(ad, visited, S, G):

    if not ad[S]: # 시작점에 연결된 간선이 없으면 종료:
        return 0
    else:
        visited[S] = True # 시작점 방문

        for i in ad[S]:
            stack = []
            stack.append(i)  # 시작점에 연결된 모든 노드 탐색
            while stack:
                x = stack.pop()
                visited[x] = True
                if ad[x]:
                    for j in ad[x]:
                        if visited[j] == False:
                            stack.append(j)

        if visited[G]:
            return 1
        else:
            return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # V 노드 수, E 간선 수
    visited = [False] * (V+1)
    ad = [[] for _ in range(V+1)] # 연결리스트
    for i in range(E):
        x, y = map(int, input().split())
        ad[x].append(y)

    S, G = map(int, input().split()) #S 시작, G 도착

    print(f'#{tc} {dfs(ad, visited, S, G)}')