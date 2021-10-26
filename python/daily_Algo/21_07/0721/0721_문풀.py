#2029 SWEA


#테스트 케이스 받기
T = int(input())
list_x =[]
list_y =[]
for i in range(T):
    x, y = map(int, input().split()) # 입력값을 받아오다
    list_x = list_x + [x] 
    list_y = list_y + [y]

for j in range(T):
    print(f'#{T} {list_x[j]//list_y[j]} {list_x[j]%list_y[j]}')