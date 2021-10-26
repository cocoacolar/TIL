N = int(input())
tmp = 1

for i in range(1, N+1):
	tmp *= i
tmp = str(tmp)
k = len(tmp)
ans = 0
for i in range(k-1, -1, -1):
	if tmp[i] == '0':
		ans += 1
	else:
		break
print(ans)
