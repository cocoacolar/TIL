def check(arr, r, c):
	if len(arr) == 5:
		for x in range(5):
			flag = False
			for y in range(5):
				if table[x][y] == 'o':
					flag = True
				else:
					flag = False
					break
			if flag:
				return 'YES'
		for c in range(5):
			flag = False
			for r in range(5):
				if table[r][c] == 'o':
					flag = True
				else:
					flag = False
					break
			if flag:
				return 'YES'
		flag = False
		for r in range(5):
			for c in range(5):
				if r==c and table[r][c] == 'o':
					flag = True
				elif r==c and table[r][c] != 'o':
					flag = False

		if flag:
			return 'YES'
		flag = False
		for r in range(5):
			for c in range(5):
				if r+c == 4 and table[r][c] == 'o':
					flag = True
				elif r+c == 4 and table[r][c] != 'o':
					flag = False

		if flag:
			return 'YES'
		return 'NO'

	for x in range(6):
		flag  = False
		count = 0
		for y in range(6):
			if arr[x+r][x+c] == 'o' and count <= 5:
				flag = True
				count += 1
			elif arr[x+r][x+c] == 'o' and count > 5:
				flag = False
				count = 0
		if flag and count == 5:
			return 'YES'
	for y in range(6):
		flag  = False
		count = 0
		for x in range(6):
			if arr[x+r][x+c] == 'o' and count <= 5:
				flag = True
				count += 1
			elif arr[x+r][x+c] == 'o' and count > 5:
				flag = False
				count = 0
		if flag and count == 5:
			return 'YES'

		count = 0
		flag = False
		for x in range(6):
			for y in range(6):
				if x+y == 5 and arr[x + r][x + c] == 'o':
					flag = True
					count += 1
				elif x+y == 5 and arr[x + r][x + c] != 'o' and count <= 4:
					flag = False
					count = 0
		if flag and count == 5:
			return 'YES'

		count = 0
		flag = False
		for x in range(6):
			for y in range(6):
				if x == y and arr[x + r][x + c] == 'o':
					flag = True
					count += 1
				elif x == y and arr[x + r][x + c] != 'o' and count <= 4:
					flag = False
					count = 0
		if flag and count == 5:
			return 'YES'
	return 'NO'

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	table = [list(input()) for _ in range(N)]

	if N == 5:
		print('#{} {}'.format(tc, check(table, 0, 0)))
	else:
		flag = False
		for r in range(N-5):
			for c in range(N-5):
				if check(table, r, c) == 'YES':
					flag = True
					break
			if flag:
				break
		if flag:
			print('#{} YES'.format(tc))
		else:
			print('#{} NO'.format(tc))
