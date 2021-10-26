# 에라토스테네스의 체 활용
def eratos(x, y):
	sieve = [True] * (y+1) # 에라토스 테네스체 초기화
	sieve[1] = False # 1이 해당하지 않도록 제외
	m = int(y ** 0.5) #제곱근 까지구하도록
	for i in range(2, m+1):
		for j in range(i+i, y+1, i):
			sieve[j] = False
	return [i for i in range(x, y+1) if sieve[i] == True] # x 이상 y이하에서 소수 구하기


x, y = map(int, input().split())
result = eratos(x, y)

for i in result:
	print(i)