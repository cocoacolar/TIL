T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split()) # N 컨테이너수 , M 트럭의 수
	box = list(map(int, input().split()))
	car = list(map(int, input().split()))
	box_used = [0] * N
	box.sort(reverse=True)
	car.sort(reverse=True)
	result = 0

	for a in range(M):
		for b in range(N):
			if car[a] >= box[b] and box_used[b]==0:
				result += box[b]
				box_used[b] = 1
				break
	print(f'#{tc} {result}')