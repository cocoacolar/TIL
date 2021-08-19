def solution(scores):
    answer = ''

    for c in range(len(scores(0))):
        test = []
        for r in range(len(scores(0))):
            test.append(scores[r][c])

        if max(test) == scores[c][c] and test.count(max(test)) == 1:
            mean = (sum(test) - scores[c][c]) / (len(test) - 1)
            if mean >= 90:
                answer += 'A'
            elif 80 <= mean < 90:
                answer += 'B'
            elif 70 <= mean < 80:
                answer += 'C'
            elif 50 <= mean < 70:
                answer += 'D'
            else:
                answer += 'F'
        elif min(test) == scores[c][c] and test.count(min(test)) == 1:
            mean = (sum(test) - scores[c][c]) / (len(test) - 1)
            if mean >= 90:
                answer += 'A'
            elif 80 <= mean < 90:
                answer += 'B'
            elif 70 <= mean < 80:
                answer += 'C'
            elif 50 <= mean < 70:
                answer += 'D'
            else:
                answer += 'F'
        else:
            mean = sum(test) / len(test)
            if mean >= 90:
                answer += 'A'
            elif 80 <= mean < 90:
                answer += 'B'
            elif 70 <= mean < 80:
                answer += 'C'
            elif 50 <= mean < 70:
                answer += 'D'
            else:
                answer += 'F'
    return answer

x = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(x))