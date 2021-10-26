T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    min_result = 1000
    min_idx = 0
    num_c = 0
    for i in range(N):
        num_c += C[i]
        C[i] = num_c

    for j in range(N):
        if abs(C[N-1]//2 - C[j]) < min_result:
            min_result = abs(C[N-1]-C[j]*2)
            min_idx = j+1

    print(f'#{tc} {min_idx} {min_result}')