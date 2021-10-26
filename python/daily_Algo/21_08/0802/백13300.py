#여학생 = 0 남학생 = 1

import sys

total, room = map(int, sys.stdin.readline().split())
student_dict = {
    10: 0, 11: 0,
    20: 0, 21: 0,
    30: 0, 31: 0,
    40: 0, 41: 0,
    50: 0, 51: 0,
    60: 0, 61: 0,
}

for k in range(total):
    x = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, 7):
        if x[1] == i and x[0] == 0:
            student_dict[i*10] += 1
            break
        elif x[1] == i and x[0] == 1:
            student_dict[i*10+1] += 1
            break
total = 0

for num in student_dict:
    
    if student_dict[num] % room == 0:
        total += student_dict[num] // room
    else:
        total += ((student_dict[num] // room)+1)

print(total)