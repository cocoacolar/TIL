#백준 2562번 브론즈2
import sys
big = 0
count = 0
for i in range(9):
    k = int(sys.stdin.readline())
    if k > big:
        big = k
        count = i + 1
print(big)
print(count)
