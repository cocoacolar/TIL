T = int(input())

x = list(map(int, input().split()))

result = []
for i in range(T):
    result.append(0)

count = 1
for k in x:
    result.insert(count-k-1, count)
    count += 1 
    
for x in range(result.count(0)):
    result.remove(0)

for j in result:
    print(j, end=' ')