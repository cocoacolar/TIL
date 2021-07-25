# 백준 1546 브1
import sys

subjects = int(input())

score_list = [score for score in map(int, sys.stdin.readline().split())]
new_score_list = []
for score in score_list:
    new_score_list.append(score/max(score_list)*100)

print(float(sum(new_score_list))/float(subjects))