T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    s_list = [input() for _ in range(N)]

    # 가로 찾기
    flag = False
    for r in range(N):
        for c in range(N-M+1):
            sen = s_list[r][c:c+M]
            if sen == sen[::-1]:
                print(f'#{tc} {sen}')
                flag = True
                break

        if flag:
            break
    else:  # 세로찾기
        for y in range(N):
            for x in range(N-M+1):
                sen = ''
                for j in range(x, x+M):
                    sen += s_list[j][y]
                if sen == sen[::-1]:
                    print(f'#{tc} {sen}')
                    flag = True
                    break
            if flag:
                break
