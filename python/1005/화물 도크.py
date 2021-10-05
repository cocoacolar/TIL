T = int(input())

for tc in range(1, T+1):
	N = int(input()) # 신청서
	time = []
	for i in range(N):
		s, e = map(int, input().split())
		time.append((s,e))
	time.sort(key=lambda x:(x[1], x[0])) #끝나는 시간 기준정렬 후 시작시간 기준 정렬
	maxV = 0
	for i in range(N):
		end_time = time[i][1]
		tmp = 1
		for j in range(i+1, N):
			if time[j][0] >= end_time:
				tmp += 1
				end_time = time[j][1]
		if maxV < tmp:
			maxV = tmp
	print(f'#{tc} {maxV}')