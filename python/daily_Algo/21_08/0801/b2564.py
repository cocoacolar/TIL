import sys

def point(x)



width, hight = map(int, input().split())

store = int(input())
sl = [] # 상점 좌표
for i in range(store):
    x = list(map(int, sys.stdin.readline().split()))
    sl.append(x)

x, y = map(int, input().split())
distance = 0

