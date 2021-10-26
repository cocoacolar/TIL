T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    ans = 0
    right = N-1
    left = N-2
    while left >= 0:
        tem = num[right] - num[left]
        if tem <= 0:
            right = left
            left = right-1
        else:
            ans += tem
            left -= 1



    print(f'#{tc} {ans}')