# N까지 입력받아 1줄로 나타내기
import sys

n = int(sys.stdin.readline())  #여러줄 입력 받을 때는 sys.stdin.readline().split() 무튼 이게 더 빠름

for i in range(1, n+1):
    print(i)