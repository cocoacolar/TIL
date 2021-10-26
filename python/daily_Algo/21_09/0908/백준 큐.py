import sys

N = int(input())
queue = [0]*10000
front = 0
rear = -1
for i in range(N):
    word = input().split(' ')
    if len(word) == 2:
        rear += 1
        queue[rear] = word[1]
    