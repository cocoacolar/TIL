T = 10
# 1은 아래로 2는 위로
for tc in range(1, T+1):
	N = int(input())
	table = [list(map(int, input().split())) for _ in range(100)]
	cnt = 0
	for c in range(N):
		flag = False  # 열 단위 초기화
		for r in range(N):
			if table[r][c] == 1: # 1떨어지기 시작
				flag = True
			elif table[r][c] == 2:
				if flag: # 2 만나면 교착 1 증가
					cnt += 1
					flag = False # 상태 초기화
	print('#{} {}'.format(tc, cnt))