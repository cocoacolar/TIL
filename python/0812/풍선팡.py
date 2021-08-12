T = int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    max_s = 0

    for r in range(M): #행
        for c in range(N): #열
            k = arr[r][c] #r-k<= 구간합<r+k+1
            r_sum = 0
            c_sum = 0
            tem_sum = 0
            if 0<=(r-k)<M and 0<=(r+k)<M: # 행 구간합 구하기
                for i in range(r-k, r+k+1):
                    r_sum += arr[i][c]
            elif 0<=(r-k)<M and (r+k)>=M:
                for i in range(r-k, M):
                    r_sum += arr[i][c]
            elif (r-k)<0 and (r+k)>=M:
                for i in range(M):
                    r_sum += arr[i][c]
            elif (r-k)<0 and 0<=(r+k)<M:
                for i in range(r+k+1):
                    r_sum += arr[i][c]


            if 0<=(c-k)<N and 0<=(c+k)<N: # 열 구간합 구하기
                for j in range(c-k, c+k+1):
                    c_sum += arr[r][j]
            elif 0<=(c-k)<N and (c+k)>=N:
                for j in range(c-k, N):
                    c_sum += arr[r][j]
            elif (c-k)<0 and (c+k)>=N:
                for j in range(N):
                    c_sum += arr[r][j]
            elif (c-k)<0 and 0<=(c+k)<N:
                for j in range(c+k+1):
                    c_sum += arr[r][j]

            tem_sum = r_sum + c_sum - k
            if max_s < tem_sum:
                max_s = tem_sum

    print(f'#{tc} {max_s}')