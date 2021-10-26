import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
	x, y = map(int, input().split())
	arr.append((x, y))
arr.sort(key=lambda x:(x[1], x[0]))

for x in arr:
	print(x[0], x[1])