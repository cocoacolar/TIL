def solution(s):
	N = len(s)
	words = []

	for i in range(1, (N // 2) + 2):
		if N%i:
			continue
		result = ''
		p = 0
		p = p + i
		tmp = s[:i]
		t = 1
		while p <= N:

			if s[p:p + i] == tmp:
				t += 1
				p = p + i
			elif s[p:p + i] != tmp:
				if t >= 2:
					tem = str(t) + tmp
					result += tem
					tmp = s[p:p + i]
					p = p + i
					t = 1
				else:
					result += tmp
					tmp = s[p:p + i]
					p = p + i
		words.append(result)
	minV = 999999
	print(words)
	for k in words:
		if len(k) < minV:
			minV = len(k)

	answer = minV
	return answer
print(solution("abcabcdede"))