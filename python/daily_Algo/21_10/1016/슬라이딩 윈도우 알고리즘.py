# 배열의 길이 N과 창문의 길이 W 입력받기
N, W = 8, 3
data = [7, 2, 4, 1, 6, 5, 8, 3]

# 각각의 값 초기 설정
tmp = 0
maxV = 0
start = 0
end = 0

# window 밀기 시작
while end < N:
	# 창문길이 맞추기
	if end-start < W:
		tmp += data[end]
		end += 1
		continue
	# 창문길이가 맞춰졌으면 최대값 비교
	tmp -= data[start]
	tmp += data[end]
	if tmp > maxV:
		maxV = tmp
	# 창문 이동
	start += 1
	end += 1

print(maxV)


