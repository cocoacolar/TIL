# B. 10871  다시 공부할것
# 리스트안에 for 문쓰는 법을 

N, X = map(int, input().split())


num_list = [num for num in input().split()]  #for문을 리스트 안으로 써서 집어 넣기 

for result in num_list:
    if int(result) < X:
        print(int(result), end=' ')


# a,b = input().split()
# a = int(a)
# b = int(b)
# num = list(map(int, input().split()))
# for i in range(a):
#     if num[i] < b :
#         print(num[i], end=" ")