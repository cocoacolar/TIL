from collections import deque


mychu = 20 #현재 마이쮸 개수
queue = deque()
queue.append(1)
m = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
t = 2
cnt = 1
while mychu>0:
    x = queue.popleft()
    k = m[x]+1
    for _ in range(k):
        if mychu == 0:
            break
        mychu -= 1

    m[x] += m[x]+1
    queue.append(x)
    queue.append(t)
    t+=1
    # print(cnt)
    # cnt += 1
    # print(m)
    # print(queue)
    print(mychu)
print(x)
