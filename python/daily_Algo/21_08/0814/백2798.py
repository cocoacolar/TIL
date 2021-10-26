N, M = map(int, input().split())

num_list = list(map(int, input().split()))
min_s = 500000000
result = 0
for a in range(len(num_list)-2):
    for b in range(a+1, len(num_list)-1):
        for c in range(b+1, len(num_list)):
            k = num_list[a]+num_list[b]+num_list[c]
            if min_s > (M-k) and k <= M:
                min_s = M-k
                result = k
print(result)