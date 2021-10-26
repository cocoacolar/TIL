N = 1000 - int(input())

money = [500, 100, 50, 10, 5, 1]
result = 0
for m in money:
	if N >= m:
		result += N//m
		N -= N//m * m

print(result)