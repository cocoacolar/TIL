# 3052번 브론즈2
import sys

x = []
for num_list in range(10):
    x.append(int(sys.stdin.readline().rstrip()))

l_list = [] # 나머지 리스트 
for num in x:
    l_list.append(num % 42)

count = 0
for i in range(42):
    if i in l_list:
        count += 1

print(count)