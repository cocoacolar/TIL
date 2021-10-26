#x만큼 떨어져있는

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    
    return answer