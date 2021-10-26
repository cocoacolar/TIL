def check(word):
    stack=[]
    for i in word:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            if stack:
                x = stack.pop()
                if x != '{':
                    return 0
            else:
                return 0
        elif i == ')':
            if stack:
                x = stack.pop()
                if x != '(':
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:

        return 1

T = int(input())

for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {check(word)}')
