def solution(n):
    k = {}
    p = 1
    while True:
        tmp = p ** 2
        if tmp > n:
            break
        k[tmp] = p
        p += 1
    if k.get(n, -1)== -1:
        return -1
    else:
        return (k.get(n, -1)+1)**2

print(solution(16))