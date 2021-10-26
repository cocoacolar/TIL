# 데이터 개수 N과 부분 연속 수열 합 M을 입력 받기
N, M = 5, 5
data = [1, 2, 3, 4, 5]

cnt = 0  # 부분 연속 수열의 수
tmp = 0  # 부분 합
end = 0

# start를 차례대로 증가 시키며 반복
for start in range(N):
	# end를 가능한 만큼 이동시키기
	# 부분합이 M보다 작거나 수열의 마지막 인덱스이면 while문 종료
	while tmp < M and end < N:
		tmp += data[end]
		end += 1
	# 부분 합이 m일 때 카운트 증가
	if tmp == M:
		cnt += 1
	tmp -= data[start]

print(cnt)

