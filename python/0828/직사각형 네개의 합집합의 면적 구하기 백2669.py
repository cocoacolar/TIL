arr = [[0]*101 for _ in range(101)]

cnt = 0
for _ in range(4):
	c1, r1, c2, r2 = map(int, input().split())
	for a in range(r1, r2):
		for b in range(c1, c2):
			if arr[a][b] == 0:
				arr[a][b] = 1
				cnt += 1

print(cnt)




