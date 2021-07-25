#백준 8958번 브론즈 2   ## 초간단 풀이가 있다....... 그랬다.... 하... 

T = int(input())

results_ox = []
for i in range(T):
    ox = input()
    ox_list = []
    for j in range(len(ox)):   #입력된 ox 문자열을 0,1리스트 형태로 변환
        if ox[j] == 'X':
            ox_list.append(0)
        else:
            ox_list.append(1)
    results_ox.append(ox_list)

for score_list in results_ox:
    answer = []
    cal = []
    for n in score_list:
        
        if n == 1:
            cal.append(1)

        else:
            answer.append(cal)
            cal = []
    answer.append(cal)
    
    rewards = 0
    for num_list in answer:
        if num_list == []:
            continue
        else:
            rewards += (len(num_list)*(len(num_list)+1))/2 
    print(int(rewards))

    
    








    
        

