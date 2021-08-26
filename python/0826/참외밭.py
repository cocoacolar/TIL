
# 동1, 북4, 서2 남3

N = int(input()) # 참외 수
k = [[] for _ in range(8)]
arr = []
for i in range(1, 7):
	d, x = map(int, input().split())
	k[d].append(x)
	arr.append(d)
a, b = 0, 0
d = [1, 4, 2, 3, 1] #방향
for j in range(4):
	if len(k[d[j]]) == 2 and len(k[d[j+1]]) == 2:
		a, b = d[j], d[j+1]

if arr[:3] == [b, a, b]:
	small = k[b][0] * k[a][0]
elif arr[:2] == [a, b] and arr[4:] == [a, b]:
	small = k[a][0] * k[b][1]
elif arr[0] == b:
	small = k[a][1] * k[b][1]
else:
	small = k[b][0] * k[a][1]

big = 1
for p in range(1, 5):
	if p not in [a, b]:
		big *= k[p][0]

print((big-small)*N)