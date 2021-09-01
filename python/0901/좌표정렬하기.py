N = int(input())
result = [(x, y) for x, y in [map(int, input().split()) for _ in range(N)]]
result.sort(key=lambda x:(x[0], x[1]))
for x, y in result:
	print(x, y)

#sorted 한번이면 해결되는 거였다.