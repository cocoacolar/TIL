T = 10

for tc in range(1, T+1):
	N = int(input())
	num = list(map(int, input().split()))
	num = [0] + num
	front = 1
	rear = 0
	flag = True
	while flag:
		for i in range(1, 6):
			x = num[front]
			x -= i
			if x <= 0:
				x = 0
				num[rear] = x
				flag = False
				break
			else:
				num[rear] = x
				front = (front+1) % 9
				rear = (rear+1) % 9
	print(f'#{tc}', end=' ')
	for a in range(rear-7, rear+1):
		print(f'{num[a]}', end=' ')
	print()

