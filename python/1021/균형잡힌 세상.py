def check(word):

	stack = []
	for i in word:
		if i == '(':
			stack.append(i)
		elif i == ')':
			if stack:
				x = stack.pop()
				if x != '(':
					return 'no'
			else:
				return 'no'
		elif i == '[':
			stack.append(i)
		elif i == ']':
			if stack:
				x = stack.pop()
				if x != '[':
					return 'no'
			else:
				return 'no'
	if stack:
		return 'no'
	else:
		return 'yes'



word = input()

while word != '.':
	print(check(word))
	word = input()
