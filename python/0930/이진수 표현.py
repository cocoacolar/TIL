T = int(input())
def change(M):
	result = ''
	if M == 0:
		return '0'
	while M:
		if M%2 == 0:
			result += '0'
		else:
			result += '1'
		M = M//2
	return result[::-1]

for tc in range(1, T+1):
	N, M = map(int, input().split())

	tmp = change(M)[::-1]
	if tmp == '0' or (len(tmp) < N):
		print(f'#{tc} OFF')
	else:
		if '0' in tmp[:N]:
			print(f'#{tc} OFF')
		else:
			print(f'#{tc} ON')
