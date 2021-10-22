def f(k, r, c, sr, sc, ans):
	if k == 2:
		if sr== r and sc == c:
			print(ans)
		if sr == r and sc+1 == c:
			print(ans + 1)
		if sr+1 == r and sc == c:
			print(ans+2)
		if sr+1 == r and sc+1 == c:
			print(ans+3)
		return

	if  (sr + k//2) <= r and (sc + k//2) <= c: # 4영역에 존재
		sr = sr + k//2
		sc = sc + k//2
		f(k//2, r, c, sr, sc, ans+(k//2*k//2)*3)

	elif (sr+k//2) <= r and (sc + k//2) > c: # 3영역
		sr = sr + k//2
		f(k//2, r, c, sr, sc, ans + (k//2*k//2)*2)

	elif (sr+k//2) > r and (sc + k//2) <= c:  # 2영역
		sc = sc + k//2
		f(k//2, r, c, sr, sc, ans+(k//2*k//2))

	elif (sr+k//2) > r and (sc + k//2) > c: # 1 영역에 존재
		f(k//2, r, c, sr, sc, ans)

N, r, c = map(int, input().split())

k = 2**N
f(k, r, c, 0, 0, 0)