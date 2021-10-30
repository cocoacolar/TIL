# 최대 힙 구현
import sys
input = sys.stdin.readline

def sh(k):
	while k >= 2:

		if heap[k//2] < heap[k]:
			heap[k//2], heap[k] = heap[k], heap[k//2]
			k= k//2
		else:
			return

def dh(k):
	if heap[k*2] > heap[2*k+1]:
		if heap[k] < heap[2*k]:
			heap[2*k], heap[k] = heap[k], heap[2*k]
			dh(2*k)
	else:
		if heap[k] < heap[2*k+1]:
			heap[2*k+1], heap[k] = heap[k], heap[2*k+1]
			dh(2*k+1)

N = int(input())
heap = [0] * 1000001
p = 0
for i in range(N):
	x = int(input())
	if x == 0:
		if p != 0:
			print(heap[1])
			heap[1] = heap[p]
			heap[p] = 0
			p -= 1
			dh(1)
		else:
			print(0)

	else:
		p += 1
		heap[p] = x
		sh(p)