T = int(input())

for tc in range(1, T+1):
	N = int(input())
	num = list(map(int, input().split()))
	maxV = -1
	for a in range(N-1):
		for b in range(a+1, N):
			new = num[a]*num[b]
			tmp = str(new)
			k = len(tmp)
			flag = False
			for i in range(k-1):
				if tmp[i] > tmp[i+1]:
					flag = True
					break
			if not flag:
				if new > maxV:
					maxV = new

	print('#{} {}'.format(tc, maxV))