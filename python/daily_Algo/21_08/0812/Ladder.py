T = 10

for tc in range(1, T+1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # y = 행
    # x = 열열

    for x in range(100):
        if arr[99][x] == 2:
            ny= 99
            nx = x

            while True:
                ny -= 1
                if ny == 0:
                    break

                if 0<=(nx-1)<100 and arr[ny][nx-1] == 1:  #왼쪽에 1
                    while True:
                        nx -= 1
                        if  (nx < 0) or arr[ny][nx] == 0:
                            nx += 1
                            break
                elif 0<=(nx+1) <100 and arr[ny][nx+1] == 1:  #오른쪽에 1
                    while True:
                        nx += 1
                        if nx >= 100 or arr[ny][nx] == 0:
                            nx -= 1
                            break
    print(f'#{tc} {nx}')