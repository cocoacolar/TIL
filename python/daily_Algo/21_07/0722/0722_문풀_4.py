# s 2050
text_list = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z' 
]

alpha = input().upper()

for spelling in alpha:
    
    for i in range(len(text_list)):
        if spelling == text_list[i]:
        
            print(i + 1, end=' ')

#############################################################
#오답 발생 내일 다시 풀어볼것
#오답 발생 원인  v를 소문자로 썻기 때문

