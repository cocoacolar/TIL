import sys
input = sys.stdin.readline

R, C, B = map(int, input().split())

arr = []
for _ in range(R):
	arr = arr + list(map(int, input().split()))

N = len(arr)
start = 0
end = 257
result = 987654321324578
high = 0

for h in range(start, end+1):
	tmp1 = 0
	tmp2 = 0

	for i in range(N):
		if arr[i] < h:
			num = h-arr[i]
			tmp1 += num
		elif arr[i] > h:
			num = arr[i]-h
			tmp2 += num

	if tmp1 > tmp2 + B:
		continue
	t = tmp1 + tmp2*2
	if t <= result:
		result = t
		high = h

print(result, high)


