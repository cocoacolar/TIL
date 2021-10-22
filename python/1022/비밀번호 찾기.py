import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = {}
for _ in range(M):
	x, y = input().split()
	arr[x] = y

for _ in range(N):
	word = input().rstrip()
	print(arr[word])
