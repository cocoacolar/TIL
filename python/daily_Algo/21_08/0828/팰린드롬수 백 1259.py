while True:
	N = input()
	if N == '0':
		break
	else:
		start = 0
		end = len(N)-1
		flag = False
		while start<end:
			if N[start] != N[end]:
				flag = True
				break
			else:
				start += 1
				end -= 1
		if flag:
			print('no')
		else:
			print('yes')
