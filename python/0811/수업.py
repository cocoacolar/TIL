# 2차원 배열

N, M  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr2 = [[0] * M for _ in range(N)]
#arr2 = [[0]*M]*N  이렇게 사용하면 얕은 복사가 발생해서 망함. 사용 불가하다!!!

# 델타배열

di = [0, 1, 0, -1]
