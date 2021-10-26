from typing import Collection


T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    if k == 1:
        print(int((n*(n+1))/2))
    elif n == 1:
        print(1)
    else:
        result = 1
        for i in range(1, k+1+n-1+1):
            result *= i
        row = 1
        for j in range(1, k+2):
            row *= j

        col =1
        for k in range(1, n):
            col *= k

        result = int(result/row/col)
        print(result)