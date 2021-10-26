#백준 10818번 브3
# 
import sys

T = int(input())
num_list = [n for n in map(int, sys.stdin.readline().split())]

print(f'{min(num_list)} {max(num_list)}')
