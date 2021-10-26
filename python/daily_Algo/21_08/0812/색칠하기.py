T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # r1, c1, r2, c2, color
    board = [[0]*10 for _ in range(10)]

    for paper in arr:  # 색종이 종이에 붙이기
        for r in range(paper[0], paper[2]+1): #행
            for c in range(paper[1], paper[3]+1):  #열
                board[r][c] += paper[4]

    count = 0
    for i in range(10): # 종이에 붙은 색종이 중 겹치는 부분 계산
        for j in range(10):
            if board[i][j] >= 3:
                count += 1

    print(f'#{tc} {count}')






