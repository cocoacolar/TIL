def solution(lottos, win_nums):
    same_num = 0
    zero_num = 0

    for i in lottos:
        if i == 0:
            zero_num += 1
        elif i in win_nums:
            same_num += 1
    maxV = same_num + zero_num
    minV = same_num
    answer = []
    if maxV == 6:
        answer.append(1)
    elif maxV == 5:
        answer.append(2)
    elif maxV == 4:
        answer.append(3)
    elif maxV == 3:
        answer.append(4)
    elif maxV == 2:
        answer.append(5)
    else:
        answer.append(6)

    if minV == 6:
        answer.append(1)
    elif minV == 5:
        answer.append(2)
    elif minV == 4:
        answer.append(3)
    elif minV == 3:
        answer.append(4)
    elif minV == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer