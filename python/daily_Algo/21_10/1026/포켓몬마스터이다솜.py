import sys
input = sys.stdin.readline
N, M = map(int, input().split())
poket_dict = {}
poket_dict2 ={}
for i in range(N):
	p = input().rstrip()
	poket_dict[p] = i+1
	poket_dict2[str(i+1)] = p
for j in range(M):
	x = input().rstrip()
	if x.isdigit():
		print(poket_dict2[x])
	else:
		print(poket_dict[x])
