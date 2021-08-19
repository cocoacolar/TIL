T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = N//10 # 계산하기 편하게 바꿈
    if X == 1:
        print(f'#{tc} 1')
    elif X == 2:
        print(f'#{tc} 3')
    else:
        num = [0, 1, 3] #인덱스 순서 맞추기 위해 0 추가
        n = 2
        while n != X:
            n += 1
            case_n = num[n-1] + num[n-2]*2 #3번째부터 직전 값 + 2번째직전 값*2 라는 규칙존재
            num.append(case_n)
        print(f'#{tc} {num[X]}')
