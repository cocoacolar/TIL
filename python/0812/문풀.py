T = int(input())

num_arr = [0]*(T+1)
for i in range(T):
    x = int(input())
    for j in range(T+1):
        if x == j:
            num_arr[j] += 1


for k in range(T+1):
    if num_arr[k] != 0:
        for l in range(num_arr[k]):
            print(k)
