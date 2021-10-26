def binary_search(start, end, x):
	# 배열의 인덱스는 정수이기에 나누어 떨어지지 않는 경우를 위해 그 몫만 취함
	mid = (start+end)//2

	# start가 end보다 큰 경우는 배열에 찾는 값이 존재하지 않는 경우임으로 0반환
	if start > end:
		print(0)
		return
	# 찾는 값이 mid라면 1 반환
	if arr[mid] == x:
		print(1)
		return
	# 찾는 값이 mid 값보다 크다면 start 를 mid+1로 변경
	elif arr[mid] < x:
		start = mid+1
		binary_search(start, end, x)

	# 찾는 값이 mid 값보다 작다면 end 를 mid-1로 변경
	elif arr[mid] > x:
		end = mid-1
		binary_search(start, end, x)

# 탐색을 위한 정렬된 배열
arr = [1, 2, 3, 4, 5, 6, 7]
# 찾으려는 값
x = 0
# 시작 인덱스
start = 0
# 끝 인덱스
end = len(arr)-1

# 이진탐색 실행
binary_search(start, end, x)

'''
실행결과
>>> 1
'''




