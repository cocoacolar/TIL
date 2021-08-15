N = int(input())
num = list(map(int, input().split()))

num.sort()
new_list = [0]*N
num_s = 0
for i in range(N):
    num_s += num[i]
    new_list[i]= num_s

print(sum(new_list))