# 1스위치 켜져 있음 0 꺼짐
# 남학생 = 자기가 받은 수의 배수 상태 변경
# 여학생  = 구간이 대칭이면서 속한 스위치 모두 변경 , 단 홀수

N = int(input()) # 스위치 개수
arr = list(map(int, input().split())) # 스위치 배열
arr = [0] + arr
S = int(input()) # 학생 수

for i in range(S):
	x, y = map(int, input().split())
	if x == 1:
		for j in range(y, N+1):
			if j%y == 0:
				arr[j] = (arr[j]+1)%2
	else:
		if (y-1) <= (N-y):
			a = 1
			b = y*2
			flag = False
			while a<b:
				tmp = arr[a:b]
				if tmp == tmp[::-1]:
					flag = True
					break
				a += 1
				b -= 1
			if flag:
				for k in range(a, b):
					arr[k] = (arr[k]+1)%2
			else:
				arr[y] = (arr[y]+1)%2
		else:
			a = y-(N-y)
			b = N+1
			flag = False
			while a<b:
				tmp = arr[a:b]
				if tmp == tmp[::-1]:
					flag = True
					break
				a += 1
				b -= 1
			if flag:
				for k in range(a, b):
					arr[k] = (arr[k]+1)%2
			else:
				arr[y] = (arr[y]+1)%2
if N <= 20:
	for i in range(1, N+1):
		print(arr[i], end=' ')
elif 20 < N <= 40:
	for i in range(1, 21):
		print(arr[i], end=' ')
	print()
	for i in range(21, N+1):
		print(arr[i], end=' ')
elif 40 < N <= 60:
	for i in range(1, 21):
		print(arr[i], end=' ')
	print()
	for i in range(21, 41):
		print(arr[i], end=' ')
	print()
	for i in range(41, N+1):
		print(arr[i], end=' ')
elif 60 < N <= 80:
	for i in range(1, 21):
		print(arr[i], end=' ')
	print()
	for i in range(21, 41):
		print(arr[i], end=' ')
	print()

	for i in range(41, 61):
		print(arr[i], end=' ')
	print()
	for i in range(61, N+1):
		print(arr[i], end=' ')
elif 80< N <= 100:
	for i in range(1, 21):
		print(arr[i], end=' ')
	print()
	for i in range(21, 41):
		print(arr[i], end=' ')
	print()

	for i in range(41, 61):
		print(arr[i], end=' ')
	print()
	for i in range(61, 81):
		print(arr[i], end=' ')
	print()
	for i in range(81, N + 1):
		print(arr[i], end=' ')
