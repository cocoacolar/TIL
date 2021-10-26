def facto(N):
    if N == 1:
        return 1
    else:
        return N * facto(N-1)


N = int(input())
if N == 0:
    print(1)
else:
    print(facto(N))