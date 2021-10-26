# 핸드폰 번호가리기

def solution(phone_number):
    test = phone_number[:]
    k = test[-4:]
    answer = k.rjust(len(phone_number), '*')
    return answer