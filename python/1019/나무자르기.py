def check(num, M):
	p = 0
	for tree in trees:
		if tree > num:
			p += (tree - num)
		if p >= M:
			return True
	return False


N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
start = 0
end = trees[-1]
while start + 1 != end:
	mid = (start+end)//2
	if check(mid, M):
		start = mid
	else:
		end = mid

print(start)