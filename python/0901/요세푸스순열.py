N, K = map(int, input().split())
stack = [0]
'1, #2, #3, 4, #5, #6, #7'
for i in range(1, N+1):
	stack.append(i)

p = 1
h = 1
result = []
while len(result) != N:
	if p%K == 0 and stack[h] != 0:
		result.append(stack[h])
		stack[h] = 0
		p += 1
		h = (h+1)%(N+1)
	elif p%K == 0 and stack[h] == 0:
		h = (h+1)%(N+1)
	elif p%K != 0 and stack[h] != 0:
		p += 1
		h = (h + 1) % (N + 1)
	elif p%K != 0 and stack[h] == 0:
		h = (h + 1) % (N + 1)
print('<', end='')
for j in result:
	if j == result[-1]:
		print(j, end='')
	else:
		print(j, end=', ')
print('>')