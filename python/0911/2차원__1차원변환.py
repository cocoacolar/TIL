def solution(board, skill):

	R = len(board)
	C = len(board[0])
	answer = R * C
	board = sum(board, [])


	for case in skill:
		if case[0] == 1:
			for x in range(case[1], case[3]+1):
				p1 = x * C
				for i in range(case[2], case[4]+1):
					board[p1+i] -= case[5]
		else:
			for x in range(case[1], case[3]+1):
				p1 = x * C
				for i in range(case[2], case[4]+1):
					board[p1+i] += case[5]
	for k in board:
		if k > 0:
			answer += 1

	return answer

solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])