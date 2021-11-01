import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
count_arr = [0] * N

tmp = 0
for i in range(N):
	tmp += arr[i]
	count_arr[i] = tmp
count_arr = [0] + count_arr
for _ in range(K):
	s, e = map(int, input().split())
	print(count_arr[e]-count_arr[s-1])

