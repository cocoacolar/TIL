import sys
input = sys.stdin.readline

N = int(input())
lope = []
for i in range(N):
	lope.append(int(input()))

lope.sort()
result = 0
for i in range(N):
	tmp = lope[i] * (N-i)
	if tmp > result:
		result = tmp
print(result)