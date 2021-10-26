#코코아 집

def solution(numbers, hand):
    answer = ''
    key_pad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [-1, 0], 5: [-1, 1], 6: [-1, 2],
        7: [-2, 0], 8: [-2, 1], 9: [-2, 2],
        '*': [-3, 0], 0: [-3, 1], '#': [-3, 2]
    }
    main_hand = ''
    if hand == 'right':
        main_hand = 'R'
    else:
         main_hand = 'L'
    
    
    l_point = '*'
    r_point = '#'
    
    
    
    for num in numbers:
        l_distance = abs(key_pad[l_point][0]-key_pad[num][0]) + abs(key_pad[l_point][1]-key_pad[num][1])
        r_distance = abs(key_pad[r_point][0]-key_pad[num][0]) + abs(key_pad[r_point][1]-key_pad[num][1])
        
        if num in [1, 4, 7]:
            answer += 'L'
            l_point = num
        elif num in [3, 6, 9]:
            answer += 'R'
            r_point = num
        else:
            if l_distance > r_distance:
                answer += 'R'
                r_point = num
            elif l_distance < r_distance:
                answer += 'L'
                l_point = num
            else:
                answer += main_hand
                if main_hand == 'L':
                    l_point = num
                else:
                    r_point = num
    
    return answer