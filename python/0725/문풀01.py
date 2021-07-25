#백준 1110번 브1

N = int(input())
first = N
result = 0
while True:
    if N < 10:
        N *= 11
        result += 1
        if N == first:
            break
    else:
        N = ((N%10) * 10) + (((N//10) + (N % 10)) % 10)
        result += 1
        if N == first:
            break

print(result)