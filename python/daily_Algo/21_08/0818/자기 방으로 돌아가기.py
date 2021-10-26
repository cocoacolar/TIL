T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [0] * (400 + 1)
    for i in range(N):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x

        if x < y and x % 2 == 0 and y % 2 == 0:  # 짝수, 짝수
            for a in range(x - 1, y + 1):
                room[a] += 1
        elif x < y and x % 2 == 0 and y % 2 != 0:  # 짝수, 홀수
            for a in range(x - 1, y + 2):
                room[a] += 1
        elif x < y and x % 2 != 0 and y % 2 != 0:  # 홀수, 홀수
            for a in range(x, y + 2):
                room[a] += 1
        elif x < y and x % 2 != 0 and y % 2 == 0: # 홀수, 짝수
            for a in range(x, y + 1):
                room[a] += 1


    print(f'#{tc} {max(room)}')