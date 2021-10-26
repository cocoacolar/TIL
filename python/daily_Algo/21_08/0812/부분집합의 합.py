
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(range(1, 13)) # 주어진 리스트
    count = 0

    for i in range(1 << 12): #총 부분 집합 구하기
        case = []
        total = 0
        for j in range(12):
            if i & (1 << j):
                case.append(num_list[j])
                total += num_list[j]

        if len(case) == N and total == K: # 해당 부분집합의 원소의 개수와 합이 같다면 count 증가
            count += 1
    print(f'#{tc} {count}')
