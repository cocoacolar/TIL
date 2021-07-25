# 백준 2577 브론즈 2

x = int(input())
y = int(input())
z = int(input())

number = str(x * y * z)

for i in range(10):
    print(number.count(str(i)))  #count 함수는 문자열 에서 찾기



