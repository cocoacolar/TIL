T = int(input())

for tc in range(1, T+1):
    words = [list(map(str, input())) for _ in range(5)]

    long = 0
    for w in words: #가장 긴 문자열 찾기
        if len(w) > long:
            long = len(w)

    for word in words: #문자열에 빈문자 추가
        if len(word) < long:
            for i in range(long-len(word)):
                word.append('')

    #세로로 읽기
    ans = ''
    for c in range(len(words[0])):
        for r in range(5):
            ans += words[r][c]


    print(f'#{tc} {ans}')