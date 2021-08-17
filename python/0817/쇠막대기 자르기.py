T = int(input())
# ()(((()())(())()))(())
for tc in range(1, T+1):
    s = input()
    new_s = []
    n = 0
    while n <= len(s)-1:
        if s[n:n+2] == '()':
            new_s.append(0)
            n = n+2
        elif s[n] == '(':
            new_s.append(1)
            n += 1
        elif s[n] == ')':
            new_s.append(-1)
            n += 1
    l = 0
    p = 0

    k = new_s.index(0)
    right = k+1
    left = k-1
while True:
        if left
            new_s.pop(k)
            k = new_s.index(0)
        elif



    print(new_s)




