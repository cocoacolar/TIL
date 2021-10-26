# b. 2439

n = int(input())

for i in range(n):
    print(('*' * (i+1)).rjust(n)) #rjust(문자열수) 를 통해 전체 오른쪽 정렬