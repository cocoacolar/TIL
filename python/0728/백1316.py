# 그룹단어 만들기
# 시간이 가장 많이 걸린 문제 ,,, 이정도 노력할 가치가 있었나 싶지만.. 
# 문자열 중에 find와 rfind를 생각하면 쉽게 풀수 있는 문제였다.
import sys

T = int(input())

error = 0  #맞는 워드인지 출력

for i in range(T):
    words = sys.stdin.readline()
    
    words_dict = {}
    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        if alpha in words:
            words_dict[alpha] = words.count(alpha)
        else:
            continue
   
    #words에서 알파벳 무엇으로 구성되어있는지 확인
    for key_alpha in words_dict:
        
        if words_dict[key_alpha] == 1:
            pass
        elif (words.rfind(key_alpha)-words.find(key_alpha)) > (words_dict[key_alpha]-1):
            
            error += 1
            break



print(T - error)   


        