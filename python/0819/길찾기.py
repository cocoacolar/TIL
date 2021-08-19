def dfs(adj):
    visitied = [False]*100 #방문여부 확인

    stack = [0] # 0부터 시작
    while stack:
        x = stack.pop()
        visitied[x] = True
        for i in adj[x]:
            if visitied[i] == False:
                stack.append(i)
    if visitied[99]:
        return 1
    else:
        return 0


T = 10

for tc in range(1, T+1):
    t, N = map(int, input().split())
    num = list(map(int, input().split()))
    adj = [[] for _ in range(100)] # 연결리스트 만들기
    for i in range(N*2):
        if i%2 == 1:
            adj[num[i-1]].append(num[i])

    print(f'#{tc} {dfs(adj)}')
