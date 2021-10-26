import sys
iunput = sys.stdin.readline

M = int(input())
k = [0] * 21
for i in range(M):
	com = input().split()
	if len(com)==1:
		if com[0] == 'all':
			for i in range(1, 21):
				k[i] = 1
		elif com[0] == 'empty':
			for i in range(1, 21):
				k[i] = 0
	else:
		if com[0] == 'add':
			k[int(com[1])] = 1
		elif com[0] == 'remove':
			if k[int(com[1])]== 1:
				k[int(com[1])] = 0
		elif com[0] == 'check':
			if k[int(com[1])] == 1:
				print(1)
			else:
				print(0)
		elif com[0] == 'toggle':
			if k[int(com[1])] == 1:
				k[int(com[1])] = 0
			else:
				k[int(com[1])] = 1

