import sys


city = int(input())
dis = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

total = 0
x_city = price[0]

for i in range(city-1):
    if price[i]*dis[i] >= dis[i]*x_city:
        total += dis[i]*x_city
        
    else:
        total += price[i]*dis[i]
        x_city = price[i]
print(total)