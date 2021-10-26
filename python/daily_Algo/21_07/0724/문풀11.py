#B. 1110
### 시간 초과 나옴 접근 방법을 문자열비교가아닌 숫자 비교뽑을 수 있게 해보자
n = input()
k = n


def small_num(x):  # 0?을 만들어주는 함수
    
    result_2 = ''
    
    if int(x) < 10:
        x = '0' + x
        result_1 = int(x[0]) + int(x[1])
        
        if result_1 < 10:
            result_2 = x[1] + str(result_1)
        else:
            result_2 = x[1] + str(result_1)[1]   
    
    else:
        result_1 = int(x[0]) + int(x[1]) 
        
        if result_1 <10:
            result_2 = x[1] + str(result_1)
            
            if result_2[0] == '0':
                result_2 = result_2[1]
        
        else:
            result_2 = x[1] + str(result_1)[1]
    
    return result_2




n_count = 0
while True:
    if small_num(n) == k:
        n_count += 1
        print(n_count)
        break
    else:
        n_count += 1
        n = small_num(n)
