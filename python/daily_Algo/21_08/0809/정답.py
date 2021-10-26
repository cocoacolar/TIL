# 오름차순 정렬
# 버블 정렬
a = [55, 7, 73, 12, 42, 78, 100, 0, -7, -500, -3958682]

for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] =a[j+1], a[j]
print(a)