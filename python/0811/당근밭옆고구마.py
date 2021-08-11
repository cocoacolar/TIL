
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    c_list = list(map(int, input().split()))
    c_list = c_list + [0]
    max_long = 0
    max_go = 0
    tmp_long = 0
    tmp_go = 0
    flag = False # 긴줄기 일때 True, 아니면 False
    count = 0
    for i in range(N):
        if c_list[i] < c_list[i+1] and c_list[i] != 0: # 0이 긴줄기에 포함되지 않게 
            tmp_long += 1
            tmp_go += c_list[i]
            flag = True
        elif c_list[i] >= c_list[i+1]:                 #긴줄기가 끊기거나, 아닌상황
             if flag:                                  # 직전까지 긴줄기였다면
                tmp_long += 1
                tmp_go += c_list[i]
                count += 1 
                if max_long < tmp_long:                #현재 긴줄기의 길이가 이전 최대 긴줄기보다 길다면 
                     max_long = tmp_long
                     max_go = tmp_go
                     tmp_long = 0
                     tmp_go = 0
                     flag = False
                elif max_long == tmp_long:              # 현재 긴줄기와 같다면 고구마 많은 긴줄기 고구마 구하기
                    if max_go < tmp_go:
                        max_go = tmp_go
                        tmp_long = 0
                        tmp_go = 0
                        flag = False
                    else:
                        tmp_long = 0
                        tmp_go = 0
                        flag = False
                else:
                    tmp_long = 0
                    tmp_go = 0
                    flag = False
    print(f'#{tc} {count} {max_go}')