N = int(input())

arr = list(list(map(str, input().rstrip())) for _ in range(N))

maxV = 0
for r in range(N):
	tmp = 0
	for c in range(N):
		if r == c:
			continue
		if arr[r][c] == 'Y':
			tmp += 1
		else:

			for y in range(N):
				flag = False
				if y == r:
					continue
				friend = 0
				for x in range(N):
					if arr[y][x] == 'Y' and (x==r or x==c):
						friend += 1
				if friend == 2:
					tmp += 1
					flag = True
				if flag:
					break


	if maxV < tmp:
		maxV = tmp

print(maxV)
