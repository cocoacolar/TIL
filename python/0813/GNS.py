T = int(input())
for tc in range(1, T+1):
    t, N = map(str, input().split())
    num = list(map(str, input().split()))

    check = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    tem = [0]*10

    for i in range(len(check)):
        for j in num:
            if check[i] == j:
                tem[i] += 1

    print(t)
    for k in range(10):
        print(f'{check[k]} '* tem[k], end=' ')




