def pre_order(n):
	global cnt
	if n:    #유효한 정점이면
		cnt += 1
		pre_order(left[n])#n의 왼쪽 자식으로 이동
		pre_order(right[n])



T = int(input())
for tc in range(1, T+1):
	E, N = map(int, input().split())
	edge = list(map(int, input().split()))
	# V개의 정점이 있는 트리의 간선 수
	left = [0]*(E+2)
	right = [0]*(E+2)
	cnt = 0
	for i in range(E):
		p, c = edge[i*2], edge[i*2+1]
		if left[p] == 0: # p의 왼쪽자식이 없으면
			left[p] = c
		else:			# 왼쪽자식이 있으면 오른쪽 자식으로 저장
			right[p] = c

	pre_order(N)
	print(f'#{tc} {cnt}')