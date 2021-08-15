T = int(input())
time = []
for tc in range(T):
    x, y = map(int, input().split())
    time.append((x,y))

time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

count = 1
end_time = time[0][1]
k = 1
while k <= T-1:
    if time[k][0] >= end_time:
        end_time = time[k][1]
        k += 1
        count += 1
    else:
        k += 1
print(count)
