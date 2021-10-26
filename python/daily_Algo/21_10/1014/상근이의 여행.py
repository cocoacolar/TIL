import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    x, y = map(int, input().split())
    for _ in range(y):
        a, b = map(int, input().split())
    print(x-1)