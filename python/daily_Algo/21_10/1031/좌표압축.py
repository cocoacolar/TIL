import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

tmp = list(set(arr[:]))
tmp.sort()
k_idx = {}
for i in range(len(tmp)):
	k_idx[tmp[i]] = i

for j in arr:
	print(k_idx[j], end=' ')