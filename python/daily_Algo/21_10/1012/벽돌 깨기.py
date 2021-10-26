from copy import deepcopy

def bomb(h, w):
	global H, W
	if tmp_arr[h][w] == 1:
		tmp_arr[h][w] = 0
		return
	k = tmp_arr[h][w]
	tmp_arr[h][w] = 0
	dr = [1, -1, 0, 0]
	dc = [0, 0, 1, -1]
	for i in range(4):
		nr = h + dr[i]
		nc = w + dc[i]
		for j in range(1, k):
			if 0<=nr<H and 0<=nc<W:
				if tmp_arr[nr][nc] == 0:
					nr += dr[i]
					nc += dc[i]
				else:
					bomb(nr, nc)
					nr += dr[i]
					nc += dc[i]


def clean(H, W, x_list):
	for c in range(W):
		for r in range(H-1, -1, -1):
			if x_list[r][c] == 0:
				t = r
				while t>-1:
					if x_list[t][c] != 0:
						x_list[r][c], x_list[t][c] = x_list[t][c], x_list[r][c]
						break
					t -= 1

	return x_list

T = int(input())
for tc in range(1, T+1):
	N, W, H = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(H)]
	tmp_list = [deepcopy(arr)]
	k = 1
	while k < N+1:
		k += 1
		nxt = [] # 1회 임시 저장
		while tmp_list:
			lst = tmp_list.pop()
			for w in range(W):
				tmp_arr = deepcopy(lst)
				for h in range(H):
					if tmp_arr[h][w] == 0: # 위에서 부터 0이면 다음행으로
						continue
					else:
						bomb(h, w)
						nxt.append(tmp_arr)
						break

		tmp_list = []
		for x_list in nxt:
			tmp_list.append(clean(H, W, x_list))

	if tmp_list:
		result = []
		for x in tmp_list:
			cnt = 0
			for r in range(H):
				for c in range(W):
					if x[r][c] != 0:
						cnt += 1
			result.append(cnt)
		ans = min(result)

	else:
		ans = 0
	print(f'#{tc} {ans}')







