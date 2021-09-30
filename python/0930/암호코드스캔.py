import sys

sys.stdin = open('sample_input.txt')


T = int(input())
change = {
	'0': '0000',
	'1': '0001',
	'2': '0010',
	'3': '0011',
	'4': '0100',
	'5': '0101',
	'6': '0110',
	'7': '0111',
	'8': '1000',
	'9': '1001',
	'A': '1010',
	'B': '1011',
	'C': '1100',
	'D': '1101',
	'E': '1110',
	'F': '1111'
}
rate = {
	'3211': 0, '2221': 1, '2122': 2,
	'1411': 3, '1132': 4, '1231': 5,
	'1114': 6, '1312': 7, '1213': 8,
	'3112': 9
}

for tc in range(1, T+1):
	R, C = map(int, input().split())
	ans = []
	wait = []
	arr_list = [input().strip() for _ in range(R)]
	for arr in arr_list:
		tmp = ''
		for i in arr:
			tmp += change[i]
		if '1' in tmp:
			code = tmp[::-1]
			n = 0 # 시작
			r1 = 0 # 비율1
			r2 = 0 # 비율2
			r3 = 0 # 비율3
			r4 = 0 # 비율4
			real_code = []
			flag = False
			dis = 0

			while n != len(code):

				if code[n] == '1' and r3 == 0:
					r4 += 1

				elif code[n] == '0' and r4>0 and r2==0 and r1==0:
					r3 += 1

				elif code[n] == '1' and r4>0 and r3>0 and r1==0:
					r2 += 1

				elif code[n] == '0' and r4>0 and r3>0 and r2>0:
					r1 += 1

				if (r1 + r2 + r3 + r4)%7 == 0 and r1 > 0 and r2 > 0 and r3>0 and r4>0:

					a = min(r1, r2, r3, r4)
					if r1%a == 0 and r2%a == 0 and r3%a == 0 and r4%a == 0 and r1//a <= 3 and r2//a <= 4 and r3//a <=4 and r4//a <= 4:
						num = str(r1//a)+str(r2//a)+str(r3//a)+str(r4//a)
						r1 = r2 = r3 = r4 = 0
						real_code.append(rate[num])


				if len(real_code) == 8:

					k = real_code[::-1]

					odd = 0
					even = 0
					last = 0
					for i in range(8):
						if i == 7:
							last = k[i]
							continue
						if i%2 !=0:
							odd += k[i]
						else:
							even += k[i]
					result = even*3 + odd + last
					x = odd + even +last

					if result % 10 == 0:
						if k not in wait:
							wait.append(k)
							ans.append(x)
					real_code = []

				n += 1
	print(f'#{tc} {sum(ans)}')




