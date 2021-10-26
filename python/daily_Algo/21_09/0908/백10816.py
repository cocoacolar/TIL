
N = int(input())
numbers =list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

result= {}
for i in range(N):
    if result.get(numbers[i], -1) == -1:
        result[numbers[i]] = 1
    else:
        result[numbers[i]] += 1

for k in check:
    if result.get(k, -1) == -1:
        print(0, end=" ")
    else:
        print(result[k], end=" ")