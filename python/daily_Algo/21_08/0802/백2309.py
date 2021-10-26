import random
small =[]
for i in range(9):
    x = int(input())
    small.append(x)


result = []
while True:
    k = random.sample(small, 7)
    if sum(k) ==  100:
        k.sort()
        for i in k:
            print(i)
        break