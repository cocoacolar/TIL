import heapq
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
	N = int(input())
	maxH = []
	minH = []

	for i in range(N):
		word, n = map(str, input().split())
