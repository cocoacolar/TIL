#S 2043번

# 5- 1 +1

number, key = map(int, input().split())
num_big = 1
num_same = 1
num_small = 1
if number > key:
    while number > key:
        number -= 1
        num_big += 1
    print(num_big)

elif number == key:
    print(num_same)

else:
    while number < key:
        number += 1
        num_small += 1
    print(num_small)




