def team(group, p):
	global maxV
	global flag
	global t
	if len(group) == N//2:
		ans = 0
		anp = 0
		for i in range(3):
			if group[i] > ans:
				ans = group[i]
				anp = p[i]
		if ans > maxV:
			maxV = ans
			t = anp
			flag = True
		return
	for a in range(N):
		if people[a] == 1:
			continue
		for b in range(a, N):
			if a == b or people[b] == 1:
				continue
			if mbti[a] == mbti[b]:
				continue
			if mbti[a][0] == 'I' and mbti[b][0] == 'I':
				continue
			if blood[a] == 'O' and blood[b] == 'O':
				continue
			if mbti[a][2] == 'T' and mbti[b][3] != 'P':
				continue
			if mbti[b][2] == 'T' and mbti[a][3] != 'P':
				continue
			sa = score[a]
			sb = score[b]
			if blood[a] == blood[b]:
				sa -= 15
				sb -= 15
			if blood[a] == 'O':
				sb += 10
			elif blood[b] == 'O':
				sa += 10

			if mbti[a][0] == 'E' and mbti[b][0] == 'E':
				sa += 20
				sb += 20

			tmp = 0
			for k in range(4):
				if mbti[a][k] == mbti[b][k]:
					tmp += 1
			ans = sa + sb
			if tmp == 3:
				ans += 40
			p.append((a, b))
			people[a] = 1
			people[b] = 1
			group.append(ans)
			team(group, p)
			group.pop()
			p.pop()
			people[a] = 0
			people[b] = 0




T = int(input())
for tc in range(1, T+1):
	N = int(input()) # 학생수
	people = [0] * N
	mbti = {}
	blood = {}
	score = {}
	maxV = 0
	flag = False
	result = []
	p = []
	t = []
	for i in range(N):
		st = list(map(str, input().split()))
		mbti[i] = st[0]
		blood[i] = st[1]
		score[i] = int(st[2])
	team(result, p)

	if t:
		t1 = t[0] + 1
		t2 = t[1] + 1
		print(f'#{tc} {t1} {t2} {maxV}')
	else:
		print(f'#{tc} -1')
