# 단계3

# 배제할 열 순서쌍 만들기
def f(N):
	ban_list = []
	for r in range(N):
		for c in range(N):
			ban_list.append((r, c))
	return ban_list


# 최소합 찾기
def findminV(y, r, k): #y 금지된 행, 시작할 행r k합
	global minV

	if sum(visited_c) == N: #모든 곳을 다 방문했다면
		if k < minV:
			minV = k
		return
	if y==r: # 금지된 행과 현재 행이 같다면 그대로 변화 없이 행만증가
		findminV(y, r + 1, k)

	if minV < k: #모든 곳을 방문하기 전에 k가 minV보다 크다면 종료
		return
	else:
		for c in range(N):
			if visited_c[c] == 0:
				visited_c[c] = 1  #방문처리 한 다음
				findminV(y, r+1, k+arr[r][c])
				visited_c[c] = 0  #리턴해오면 방문처리 취소


T = int(input())
for tc in range(1, T+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]
	# 사용하지 않을 행,렬 순서쌍
	ban_list = f(N)

	# 최소합 구하기
	minV = 999999999

	for y, x in ban_list:
		visited_c = [0] * N  # 방문한 열의 중복을 방지하기위해
		visited_c[x] = 1 # 금지된 행을 미리 방문처리
		findminV(y, 0, 0)

	print(f'#{tc} {minV}')