def change(k):
	output = ''
	for j in range(3, -1, -1):
		output += '1' if k & (1 << j) else '0'

	return output

T = int(input())

for tc in range(1, T+1):
	N, num = map(str, input().split())
	N = int(N)
	result = ''
	for k in num:
		if k.isdigit():
			result += change(int(k))
		elif k == 'A':
			k = 10
			result += change(int(k))
		elif k == 'B':
			k = 11
			result += change(int(k))
		elif k == 'C':
			k = 12
			result += change(int(k))
		elif k == 'D':
			k = 13
			result += change(int(k))
		elif k == 'E':
			k = 14
			result += change(int(k))
		elif k == 'F':
			k = 15
			result += change(int(k))
	print(f'#{tc} {result}')
