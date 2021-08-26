def check(arr):
	cnt = 0
	for r in range(5):
		tmp = 0
		for c in range(5):
			if arr[r][c] == 0:
				tmp += 1
		if tmp == 5:
			cnt += 1
	for c in range(5):
		tmp = 0
		for r in range(5):
			if arr[r][c] == 0:
				tmp += 1
		if tmp == 5:
			cnt += 1
	tmp = 0
	for r in range(5):
		for c in range(5):
			if arr[r][c] == 0 and r==c:
				tmp += 1
		if tmp == 5:
			cnt += 1
	tmp = 0
	for r in range(5):
		for c in range(5):
			if arr[r][c] == 0 and r+c == 4:
				tmp += 1
		if tmp == 5:
			cnt += 1
	return cnt


def bingo(arr, call):
	cnt = 0
	for r in range(5):
		for c in range(5):
			k = call[r][c]
			cnt += 1
			flag = False
			for x in range(5):
				for y in range(5):
					if k == arr[x][y]:
						arr[x][y] = 0
						flag = True
						break
				if flag:
					break
			if check(arr) >= 3:
				return cnt



arr = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

print(bingo(arr, call))
