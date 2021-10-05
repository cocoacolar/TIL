T = int(input())

for tc in range(1, T+1):
	arr = list(map(int, input().split()))
	first_flag = False #홀수 베이비진 여부
	second_flag = False#짝수 베이비진 여부
	first = [0, 0]+[0] * 10 + [0, 0]
	second = [-1, -1]+[0] * 10 + [-1, -1]
	for i in range(12):
		if i%2: #홀수 이면
			second[arr[i]+2] += 1
			if second[arr[i]+2] == 3:
				second_flag = True
				break
			if second[arr[i]] >=1 and second[arr[i]+1] >= 1 and second[arr[i]+2] >= 1:
				second_flag = True
				break
			if second[arr[i]+1] >=1 and second[arr[i]+2] >= 1 and second[arr[i]+3] >= 1:
				second_flag = True
				break
			if second[arr[i]+2] >=1 and second[arr[i]+3] >= 1 and second[arr[i]+4] >= 1:
				second_flag = True
				break
		else: #짝수이면
			first[arr[i]+2] += 1
			if first[arr[i]+2] == 3:
				first_flag = True
				break
			if first[arr[i]] >=1 and first[arr[i]+1] >= 1 and first[arr[i]+2] >= 1:
				first_flag = True
				break
			if first[arr[i]+1] >=1 and first[arr[i]+2] >= 1 and first[arr[i]+3] >= 1:
				first_flag = True
				break
			if first[arr[i]+2] >=1 and first[arr[i]+3] >= 1 and first[arr[i]+4] >= 1:
				first_flag = True
				break
	if first_flag:
		print(f'#{tc} 1')
		continue
	if second_flag:
		print(f'#{tc} 2')
		continue
	print(f'#{tc} 0')

