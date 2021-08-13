T = 10
for tc in range(1, T+1):
    k = input()
    x = input()
    stc = input()
    count = 0
    k = len(x)
    for i in range(len(stc)-k+1):
        if stc[i:i+k] == x:
            count += 1
    print(f'#{tc} {count}')