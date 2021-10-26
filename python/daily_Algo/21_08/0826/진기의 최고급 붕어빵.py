T = int(input())

for tc in range(1, T+1):
	N, M, K = map(int, input().split()) #N 사람수, M 붕어빵 만드는 시간, K M초 마다 만드는 붕어수
	line = list(map(int, input().split())) # 붕어사러 오는 인간
	arr = [0]*11112
	for i in line:
		arr[i] += 1
	sell = 0
	flag = False
	for time in range(11112):
		if arr[time]:
			boong = (time//M * K) - sell
			if boong - arr[time] < 0:
				flag = True
				break
			else:
				sell += arr[time]

	if flag:
		print('#{} Impossible'.format(tc))
	else:
		print('#{} Possible'.format(tc))