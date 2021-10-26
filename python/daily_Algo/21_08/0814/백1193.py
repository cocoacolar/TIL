x = int(input())
t = 0
for i in range(1, 100000000):
    if x-(i*(i+1)/2)<=0:
        t = i
        break
k = ((t-1)*(t)/2)
y = x-k
if t%2 == 0:
    print(f'{int(y)}/{int(t+1-y)}')
else:
    print(f'{int(t+1-y)}/{int(y)}')