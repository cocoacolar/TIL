import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	a, b = map(int, input().split())
	for i in range(b):
		a = (a*a)%10
	if  a == 0:
		print(10)
	else:
		print(a)