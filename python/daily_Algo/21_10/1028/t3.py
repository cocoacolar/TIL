def solution(n):
	answer = 0
	start = 1
	end = 1
	tmp = 1
	while end < n+1:
		if tmp == n:
			answer += 1

			end += 1
			tmp += end
		elif tmp < n:
			end += 1
			tmp += end
		elif tmp > n:
			tmp -= start
			start += 1

	return answer

print(solution(15))
