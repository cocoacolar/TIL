T = int(input())

for tc in range(1, T+1):
	N = float(input())
	result = ''
	cnt = 0
	i = 1
	flag = False
	while N != 0:
		if cnt == 13:
			flag = True
			break
		if N < 2**-i:
			result += '0'
			cnt += 1
		else:
			result += '1'
			cnt += 1
			N -= 2**-i
		i += 1

	if flag:
		print(f'#{tc} overflow')
	else:
		print(f'#{tc} {result}')


