import sys
input = sys.stdin.readline
N = int(input())
order_list = []
for i in range(N):
	age, name = input().split()
	order_list.append((int(age), name, i))

order_list.sort(key=lambda x:(x[0], x[2]))

for i in order_list:
	print(i[0], i[1])