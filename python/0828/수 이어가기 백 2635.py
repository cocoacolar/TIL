n = int(input())

max_len = 0
max_li = []
for second in range(1, n + 1):
	li = [n]
	li.append(second)

	while True:
		value = li[-2] - li[-1]
		if value >= 0:
			li.append(value)
		else:
			break

	if max_len < len(li):
		max_len = len(li)
		max_li = li.copy()

print(max_len)
print(*max_li)