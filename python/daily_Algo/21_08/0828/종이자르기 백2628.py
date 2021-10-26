c, r = map(int, input().split())
N = int(input())
# 가로 0  세로1
hor = []
ver = []

for i in range(N):
	a, b = map(int, input().split())
	if a == 0:
		hor.append(b)
	else:
		ver.append(b)
hor.sort()
ver.sort()
hor = [0] + hor + [r]
ver = [0] + ver + [c]
newR = []
newC = []
for a in range(len(hor)-1):
	k = hor[a+1] - hor[a]
	newR.append(k)
for b in range(len(ver)-1):
	k = ver[b+1] - ver[b]
	newC.append(k)

maxV = 0
for x in newR:
	for y in newC:
		tmp = x * y
		if tmp > maxV:
			maxV = tmp
print(maxV)