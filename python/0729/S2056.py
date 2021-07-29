T  = int(input())


for i in range(T):
    word = input()

    if word[4:6] in ['01','03', '05', '07', '08', '10', '12']:
        pass
        if word[6] <= 3 and (word[6] == 3 and  word[7] <= 1) and (word[6:8] != '00'):
            print(f'#{i+1} {word[0:4]}/{word[4:6]}/{word[6:8]}')
        else:
            print(f'#{i+1} -1')
    elif word[4:6] in ['04','06', '09', '11']:
        pass
        if word[6] <= 3 and (word[6] == 3 and word[7] == 0) and (word[6:8] != '00'):
            print(f'#{i+1} {word[0:4]}/{word[4:6]}/{word[6:8]}')
        else:
            print(f'#{i+1} -1')
    elif word[4:6] == '02':
        pass
        if word[6] <= 2 and (word[6] == 2 and word[7] <= 8) and (word[6:8] != '00'):
            print(f'#{i+1} {word[0:4]}/{word[4:6]}/{word[6:8]}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')
