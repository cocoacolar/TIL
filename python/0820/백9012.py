import sys
T = int(input())

for tc in range(1, T+1):
    VPS = sys.stdin.readline().rstrip()
    stack = []
    for i in VPS:
        if i == '(':
            stack.append(i)
        else:
            if stack :
                x = stack.pop()
                if x != '(':
                    stack.append(x)
            else:
                stack.append(i)

    if stack:
        print('NO')
    else:
        print('YES')