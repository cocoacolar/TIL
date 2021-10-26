def d(n):
    num_chr = str(n)
    for i in range(len(num_chr)):
        n += int(num_chr[i])
    return n



b = list(range(1, 10001))

for k in range(1, 10001):
    if d(k) in b:
        b.remove(d(k))

for i in b:
    print(i)