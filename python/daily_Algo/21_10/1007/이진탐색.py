
T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())
	arr_N = list(map(int, input().split()))
	arr_N.sort()
	arr_M = list(map(int, input().split()))
	cnt = 0
	for i in arr_M:
		if i > arr_N[-1]:
			continue
		if i < arr_N[0]:
			continue
		L = 0
		R = N-1
		L_flag = False
		R_flag = False
		tmp = 0
		while L <= R:
			mid = (L+R)//2
			if arr_N[mid] == i:
				cnt += 1
				break
			elif arr_N[mid] > i and tmp == 0:
				R_flag = False
				L_flag = True
				R = mid - 1
				tmp = 1
			elif arr_N[mid] < i and tmp == 0:
				R_flag = True
				L_flag = False
				L = mid + 1
				tmp = 1
			elif (arr_N[mid] > i and R_flag == True):
				R_flag = False
				L_flag = True
				R = mid-1

			elif (arr_N[mid] < i and L_flag == True):
				R_flag = True
				L_flag = False
				L = mid+1
			else:
				break

	print(f'#{tc} {cnt}')