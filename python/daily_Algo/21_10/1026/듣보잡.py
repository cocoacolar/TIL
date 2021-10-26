import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = set([input().rstrip() for _ in range(N)])
S = set([input().rstrip() for _ in range(M)])
ans = list(L & S)
ans.sort()
print(len(ans))
for i in ans:
	print(i)