# 로또 최고 순위 최저 순위


def solution(lottos, win_nums):
    answer = []
    
    count_zero = lottos.count(0)
    new_win = []
    for num_x in win_nums:
        if num_x in lottos:
            new_win.append(num_x)
            
    rank_dict = {
        6: 1, 5: 2, 4: 3,
        3: 4, 2: 5, 1: 6,
        0: 6 
    }
    
    r_high = len(new_win) + count_zero
    r_low = len(new_win)
    answer.append(rank_dict[r_high])
    answer.append(rank_dict[r_low])
    
    
    
    
    
    return answer