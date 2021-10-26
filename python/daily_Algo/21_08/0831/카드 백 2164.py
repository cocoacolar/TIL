from collections import deque

N = int(input())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
if N != 1:

    while True:
        h = queue.popleft()

        if len(queue) == 1:
            k = queue.popleft()
            break
        k = queue.popleft()
        queue.append(k)
    print(k)
else:
    print(1)
