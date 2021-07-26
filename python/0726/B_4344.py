# # B 4344 평균은 넘겠지

T = int(input())

for i in range(T): # T 테스트 케이스 만큼 시행
    x = list(map(int, input().split()))
    a = x[0]
    b = sum(x[1:])
    result = (b/a) # 반 평균
    count = 0
    for student in x[1:]:
        if student > result:
            count += 1 


    print(f'{count/a*100: .3f}%'.lstrip())


