def check(r, tmp):
	group[r] = tmp
	for i in adjL[r]:
		if group[i] == 0:
			check(i, tmp)

T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr = list(map(int, input().split()))
	adjL = [[] for _ in range(N+1)]
	for i in range(M):
		adjL[arr[2*i]].append(arr[(2*i)+1])
		adjL[arr[(2*i)+1]].append(arr[2*i])
	group = [0]*(N+1)
	tmp = 1
	for k in range(1, N+1):
		if group[k] == 0:
			check(k, tmp)
			tmp += 1

	print(f'#{tc} {tmp-1}')