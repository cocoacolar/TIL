def check(r, c, k):
	blueflag = False
	whiteflag = False
	global blue, white
	for y in range(r, r+k):
		for x in range(c, c+k):
			if paper[y][x] == 1 and whiteflag==True:
				return False
			elif paper[y][x] == 0 and blueflag == True:
				return False
			elif paper[y][x] == 0 and blueflag == False:
				whiteflag = True
			elif paper[y][x] == 1 and whiteflag==False:
				blueflag = True
	if blueflag:
		blue += 1
		return 'blue'
	elif whiteflag:
		white += 1
		return 'white'


def cut(r, c, N):
	tmp = check(r, c, N)
	if tmp == 'white' or tmp == 'blue':
		return
	else:
		# 1영역
		cut(r, c, N//2)
		# 2영역
		cut(r, c+N//2, N//2)
		# 3영역
		cut(r+N//2, c, N//2)
		# 4영역
		cut(r+N//2, c+N//2, N//2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0
cut(0, 0, N)
print(white)
print(blue)