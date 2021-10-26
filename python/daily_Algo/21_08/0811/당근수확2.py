
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    c_list = list(map(int, input().split()))
    result = 0 
    dis = [] # 구간별 왕복 횟수 담을 리스트
    for i in range(N): # 왕복 횟수 구하고 나머지는 다음번 배열로 더하기
        if i == N-1:
            if c_list[i] == 0:
                dis.append(0)
            elif c_list[i]%M == 0:
               dis.append(c_list[i]//M)
            elif c_list[i]%M > 0:
                 dis.append((c_list[i]//M) + 1)
        
        elif c_list[i] >= M:
            dis.append(c_list[i]//M)
            c_list[i+1] += c_list[i]%M
        
        elif c_list[i] < M:
            c_list[i+1] += c_list[i]%M
            dis.append(0)
    
    for i in range(N):# 총 이동거리 구하기
        result += 2*(i+1)*dis[i]
    print(f'#{tc} {result}')