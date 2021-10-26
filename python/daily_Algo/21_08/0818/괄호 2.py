s = input()
stack = [''] * 100
top = -1
ans = 1
for x in s: # 한 글자씩 읽어서
    if x == '(': # push(x)
        top += 1
        stack[top] = x
    elif x == ')': # pop한 결과와 비교/ 스택이 비어있으면 오류(중단).
        if top>=0:
            top -= 1
            stack[top+1] # 소괄호만 있으므로 비교 생략
        else:
            ans = 0
            break
    else:
        pass

if ans and top>=0:
    ans = 0
print(ans)