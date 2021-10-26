T = int(input())
for tc in range(1, T+1):
    b_stop = [0]*5001

    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            b_stop[j] += 1

    P = int(input())
    f_p = []
    for k in range(P):
        x = int(input())
        f_p.append(x)

    print(f'#{tc}', end=' ')
    for l in f_p:
        print(b_stop[l], end=' ')

    print()

