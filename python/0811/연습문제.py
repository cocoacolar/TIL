
x = [[False] * 5 for _ in range(5)]
print(x)
count = 1
dr = [0, 1, -0, -1] #동 남 서 북
dc = [1, 0, -1,  0]
r = 0
c = -1
k = 0
while count <= 25:
    nr = r + dr[k]
    nc = c +dc[k]
    if  0<=nr<5 and  0<=nc<5 and x[nr][nc] == False:
        x[nr][nc] = count
        count += 1
        r, c = nr, nc
    else:
        k = (k+1)%4

for i in x:
    print(i)