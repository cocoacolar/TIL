# 고정비용 A , 가변비용B , 노트북 수입 C


A, B, C = map(int, input().split())



if B >= C:
    print(-1)
else:
    
    print(A//(C - B)+1)