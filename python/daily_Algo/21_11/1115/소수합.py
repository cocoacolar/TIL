def check(k):
	p = int(k**(1/2)+1)
	for i in range(1, p):
		if i == 1:
			continue
		else:
			if k%i == 0:
				return False
	return True



N = int(input())

arr = []

for k in range(2, ((N//2)+2)):
	if check(k):
		arr.append(k)
arr = arr + [0]
s = 0
e = 0
tmp = arr[0]
ans = 0

while e < len(arr)-1:

	if tmp == N:
		ans += 1
		tmp -= arr[s]
		s += 1
	elif tmp > N:
		tmp -= arr[s]
		s += 1
	elif tmp < N:
		e += 1
		tmp += arr[e]
if check(N):
	print(ans + 1)
else:
	print(ans)

