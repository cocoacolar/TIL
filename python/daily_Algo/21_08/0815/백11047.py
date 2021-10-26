N, K = map(int, input().split())
arr = []
for tc in range(N):
    num = int(input())
    arr.append(num)

arr.sort(reverse=True)

count = 0
for x in arr:
    if K == 0:
        break

    if K >= x:
        count += K//x 
        K = K%x  
print(count)