T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(10):
        for j in range(i+1,N):
            if i%2==0 and num[i]<num[j]:
                num[i], num[j] = num[j], num[i]

            elif i%2!=0 and num[i]>num[j]:
                num[i], num[j] = num[j], num[i]


    print(f'#{tc}', end=' ')
    for k in range(10):
        print(num[k], end=' ')
    print()