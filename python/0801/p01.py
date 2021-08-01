# k 번째 수 구하기 (lambda로 다시 풀어보기)

def solution(array, commands):
    answer = []
    
    
    for command in commands:        
        
        x = command[0]
        y = command[1]
        z = command[2]
        
        if x < y:
            test = array[x-1:y]
            test.sort()
            answer += [test[z-1]] 
        elif x > y:
            test = array[y-1:x]
            test.sort()
            answer += [test[z-1]]
        else:    
            test = array[x-1]
            answer += [test]
        
    
    return answer

