T = 1
# ()(((()())(())()))(())
for tc in range(1, T+1):
    s = '()(((()())(())()))(())'
    p = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            p += 1
        else:
            if s[i-1] == '(':
                p -= 1
                ans += p
            else:
                p -= 1
                ans += 1
    print(f'#{tc} {ans}')




