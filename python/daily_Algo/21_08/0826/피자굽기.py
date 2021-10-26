T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split()) #N 화덕 크기, M 피자 개수
	arr = list(map(int, input().split()))  # 피자 치즈 양
	# 7 2 6 5 3
	# 초기에 화덕에 피자 채우기
	box = []
	box_idx = []
	for i in range(N):
		box.append(arr[i])
		box_idx.append(i)
	p1 = N # 다음 들어갈 피자
	p2 = 0  # 화덕안
	while True:
		if p1 == M:
			while True:
				box[p2] = box[p2] // 2
				if sum(box) == 0:

					break
				else:
					p2 = (p2 + 1) % N
			break
		else:
			while True:
				box[p2] = box[p2]//2
				if box[p2] == 0:
					break
				else:
					p2 =(p2+1)% N

			box[p2] = arr[p1]
			box_idx[p2] = p1
			p1 += 1
			p2 = (p2 + 1) % N

	print('#{} {}'.format(tc, box_idx[p2]+1))