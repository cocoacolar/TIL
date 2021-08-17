T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())
    al = len(A)
    bl = len(B)
    cnt = 0
    n = 0
    while n <= al-bl:
        if A[n:n+bl] == B:
            cnt += 1
            n = n+bl
        else:
            n += 1
    ans = al-cnt*bl+cnt

    print(f'#{tc} {ans}')
