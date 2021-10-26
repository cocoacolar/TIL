from collections import deque
import sys
N = int(input())
queue = deque()
for i in range(N):
    word = sys.stdin.readline().rstrip().split(' ')
    
    if len(word) == 2:
        queue.append(word[1])
    else:
        if word[0] == 'front':
            if queue:
                x = queue.popleft()
                print(x)
                queue.appendleft(x)
            else:
                print(-1)
        elif word[0] == 'pop':
            if queue:   
                x = queue.popleft()
                print(x)
            else:
                print(-1)
        elif word[0] == 'size':
            print(len(queue))
        elif word[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif word[0] == 'back':
            if queue:
                x = queue.pop()
                print(x)
                queue.append(x)
            else:
                print(-1)

