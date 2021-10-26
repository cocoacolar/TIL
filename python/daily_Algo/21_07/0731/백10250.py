# 빈공간을 0으로 채우자 z fil~!!!!!!!!!!

import sys

T = int(sys.stdin.readline())
result = ''
for x in range(T):
    H, W, N =  map(int, sys.stdin.readline().split())
    
    if N % H == 0:
        x = str(H)
        y = str(N//H)
        if len(y) == 1:
            result = x + '0' + y
        else:
            result = x + y
    else:
         x = str(N%H)
         y = str(N//H + 1)
        
         if len(y) == 1:
            result = x + '0' + y
         else:
            result = x + y
    print(result)
    



    