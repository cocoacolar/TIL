
# 체육복 빌려주기 -> 그리디 알고리즘

def solution(n, lost, reserve):
    
    answer = 0
    new_lost = []
    new_reserve = []
    
    for l in lost:
        if l not in reserve:
            new_lost.append(l)
    
    for r in reserve:
        if r not in lost:
            new_reserve.append(r)
    
    answer = n - len(new_lost)

    for s in new_lost:
        if s+1 in new_reserve:
            answer += 1
            new_reserve.remove(s+1)
        elif s-1 in new_reserve:
            answer += 1
            new_reserve.remove(s-1)
    
    return answer