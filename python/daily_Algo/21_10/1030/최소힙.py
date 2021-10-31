import sys
input = sys.stdin.readline

def insert(p):
	if p == 1:
		return
	else:
		if h[p//2] > h[p]:
			h[p // 2], h[p] = h[p], h[p // 2]
			insert(p//2)

def pop_n(num):
	if h[num*2] and h[num*2+1]:
		if h[num*2] < h[num*2+1]:
			if h[num] > h[num*2]:
				h[num], h[num*2] = h[num*2], h[num]
				pop_n(num*2)
		elif h[num*2] > h[num*2+1]:
			if h[num] > h[num * 2+1]:
				h[num], h[num*2+1] = h[num*2+1], h[num]
				pop_n(num*2+1)
		elif h[num*2] == h[num*2+1]:
			if h[num*2] < h[num]:
				h[num], h[num * 2] = h[num * 2], h[num]

	elif h[num*2] and h[num*2+1] == 0:
		if h[num*2] < h[num]:
			h[num], h[num * 2] = h[num * 2], h[num]



N = int(input())
h = [0] * (11)
p = 0
for _ in range(N):
	x = int(input())

	if x == 0:
		if p == 0:
			print(0)
		else:
			print(h[1])
			h[1] = h[p]
			h[p] = 0
			p -= 1
			pop_n(1)
			# 여기서 부터 작업필요
	else:
		p += 1
		h[p] = x
		insert(p)
	print(h)