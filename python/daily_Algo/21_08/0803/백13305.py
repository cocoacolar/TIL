# 그리디 알고리즘 적용 58점 부분점수 맞음
import sys


def min_find(list_x):
    x = list_x.index(min(list_x))
    result = list_x[:x]
    return result, x


city = int(input())
long = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
price = price[:city-1]
result = 0
while True:
    k = min_find(price)
    
    result += sum(long[k[1]:])*price[k[1]]
    
    price = k[0]
    long = long[:k[1]]

    if k[0] == []:
        print(result)
        break