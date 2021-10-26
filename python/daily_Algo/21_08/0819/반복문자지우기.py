T = int(input())

for tc in range(1, T+1):
    word = input()

    stack = [] #확인할 스택
    for i in word:
        if not stack: # 스택이 비어있다면 추가
            stack.append(i)
        else:
            w = stack.pop()
            if w != i:
                stack.append(w)
                stack.append(i)

    print(f'#{tc} {len(stack)}')

