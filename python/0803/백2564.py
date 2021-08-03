
import sys

store_list = []

w, h = map(int, sys.stdin.readline().split())
s_num = int(input())
for i in range(s_num):
    s = list(map(int, sys.stdin.readline().split()))
    store_list.append(s)

dg = list(map(int, input().split()))
result = 0
for store in store_list:
    if dg[0]== 1:
        if store[0] == 1:
            result += abs(dg[1]-store[1])
        elif store[0] == 2 and h+dg[1]+store[1] <= (w+h):
            result +=  h+dg[1]+store[1]
        elif store[0] == 2 and h+dg[1]+store[1] > (w+h):
            result +=  2*(w+h)-(h+dg[1]+store[1])
        elif store[0] == 3:
            result += dg[1]+store[1]
        elif store[0] == 4:    
            result += w-dg[1]+store[1]

    elif dg[0]== 2:
        if store[0] == 1 and h+dg[1]+store[1] <= (w+h):
            result += h+dg[1]+store[1]
        elif store[0] == 1 and h+dg[1]+store[1] > (w+h) :
            result +=  2*(w+h)-(h+dg[1]+store[1])
        elif store[0] == 2:
            result +=  abs(dg[1] - store[1])
        elif store[0] == 3:
            result += dg[1] + h-store[1]
        elif store[0] == 4:    
            result += w-dg[1]+h-store[1]

    elif dg[0]== 3:
        if store[0] == 1:
            result += dg[1]+store[1]
        elif store[0] == 2:
            result +=  dg[1] + h-store[1]
        elif store[0] == 3:
            result +=  abs(dg[1] - store[1])
        elif store[0] == 4 and dg[1] + store[1] + w <= w+h:
            result += dg[1] + store[1] + w
        elif store[0] == 4 and dg[1] + store[1] + w > w+h:    
            result += 2*(w+h)-(dg[1] + store[1] + w)
    
    elif dg[0]== 4:
        if store[0] == 1:
            result += dg[1]+w-store[1]
        elif store[0] == 2:
            result +=  h-dg[1] + w-store[1]
        elif store[0] == 3 and dg[1] + store[1] + w <= w+h:
            result +=  dg[1] + store[1] + w
        elif store[0] == 3 and dg[1] + store[1] + w > w+h:
            result += 2*(w+h)-(dg[1] + store[1] + w)
        elif store[0] == 4:    
            result += abs(dg[1] - store[1])

        
print(result)
