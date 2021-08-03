def solution(price, money, count):
    answer = 0
    price_list = []    
    for i in range(1, count+1):
        price_list.append(i * price)
    
    if sum(price_list) <= money:
        return 0
    else:
        return sum(price_list) - money