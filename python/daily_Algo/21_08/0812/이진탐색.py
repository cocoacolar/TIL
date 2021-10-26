T = int(input())

for tc in range(1, T+1):
    P, fa, fb = map(int, input().split())
    L = 1
    R = P
    C = int((L+R)/2)
    count_a = 0
    while (C != fa):
        count_a += 1
        if C < fa:
            L = C
            C = int((L+R)/2)
        elif C > fa:
            R = C
            C = int((L+R)/2)
    L = 1
    R = P
    C = int((L + R) / 2)
    count_b = 0
    while (C != fb):
        count_b += 1
        if C < fb:
            L = C
            C = int((L+R)/2)
        elif C > fb:
            R = C
            C = int((L+R)/2)

    if count_a < count_b:
        print(f'#{tc} A')
    elif count_a == count_b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
