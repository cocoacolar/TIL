import sys

x = int(input())
new_word_list = []


for i in range(x):
    r, words =  sys.stdin.readline().split()
    box = ''
    for i in words:
        box += (i*int(r))
    new_word_list.append(box)

for k in new_word_list:
    print(k)