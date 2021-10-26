def solution(new_id):
    answer = new_id.lower()
    test = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '-', '_', '.'
    ]

    test_name = answer
    for i in answer:
        if i not in test:
            test_name = test_name.replace(i, '', 1)

    answer = test_name


    test_name = answer
    stack = []
    for j in test_name:
        if not stack:
            stack.append(j)
        else:
            x = stack.pop()
            if x == '.' and j == '.':
                stack.append(j)
            elif x == '.' and j != '.':
                stack.append(x)
                stack.append(j)
            elif x != '.' :
                stack.append(x)
                stack.append(j)
    answer = ''
    for k in stack:
        answer += k


    while answer[0] =='.' or answer[-1] == '.':
        if len(answer) == 1:
            answer = ''
            break
        if answer[0] =='.':
            answer = answer[1:]
        elif answer[-1] == '.':
            answer = answer[:-1]

    if not answer:
        answer += 'a'
    else:
        if len(answer) >15:
            answer = answer[:15]
            while answer[0] =='.' or answer[-1] == '.':
                if len(answer) == 1:
                    answer = ''
                    break
                if answer[0] =='.':
                    answer = answer[1:]
                elif answer[-1] == '.':
                    answer = answer[:-1]

    if len(answer) <=2:
        while len(answer) != 3:
            answer += answer[-1]



    return answer