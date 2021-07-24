# B 15552

import sys

T = int(input())

for i in range(1, T+1):
    x, y = map(int, sys.stdin.readline().split())
    print(x + y)
