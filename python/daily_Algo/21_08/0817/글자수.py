T = int(input())

for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    m_cnt = 0


    for a in s1:
        cnt = 0
        for b in s2:
            if a == b:
                cnt += 1

        if cnt > m_cnt:
            m_cnt = cnt

    print(f'#{tc} {m_cnt}')