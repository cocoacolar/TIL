T = 10

for tc in range(1, T+1):
    t = int(input())
    arr = [input() for _ in range(100)]

    #가로에서 찾기
    m_len = 0
    for r in range(100):
        for k in range(1, 101): # 회문의 길이
            for c in range(100-k+1): # 열에서 회문순회
                sen = arr[r][c:c+k]
                if sen == sen[::-1]:
                    if len(sen) > m_len:
                        m_len = len(sen)

    for y in range(100):
        for j in range(1, 101):
            for x in range(100-j+1):
                word = ''
                for p in range(x, x+j):
                    word += arr[p][y]
                if word == word[::-1]:
                    if len(word) > m_len:
                        m_len = len(word)

    print(f'#{tc} {m_len}')