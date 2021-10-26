def check(table, r, c):
	minV = 100
	check1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
	check2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
	for a in range(r-7):
		for b in range(c-7):

			tmpA = 0
			tmpB = 0
			for x in range(8):
				for y in range(8):
					if table[x+a][y+b] != check1[x][y]:
						tmpA += 1
			for x in range(8):
				for y in range(8):
					if table[x+a][y+b] != check2[x][y]:
						tmpB += 1
			if tmpA >= tmpB:
				tmp = tmpB
			else:
				tmp = tmpA

			if minV > tmp:
				minV = tmp
	return minV



r, c = map(int, input().split())
table = [list(map(str, input())) for _ in range(r)]
print(check(table, r, c))
