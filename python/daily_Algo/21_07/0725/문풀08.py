# 백준 2577 브론즈 2
import sys

multiple = []   
for num in range(3):
   multiple += [int(sys.stdin.readline().rstrip())]

result_chr = 1  # 세 숫자곱을 담을 변수
for a in range(3):
    result_chr *= multiple[a] 

result = []  #. 결과를 문자 리스트로 만들기
for k in range(len(str(result_chr))):
    result.append(str(result_chr)[k])


for number in range(10):
    count = 0
    for kill_number in result:
        if number == int(kill_number):
            count += 1
    print(count)




