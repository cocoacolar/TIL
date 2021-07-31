A, B, V = map(int, input().split())

day = 1

new_high = V - A

day_high = A-B

if new_high % day_high == 0:
    day = 1 + (new_high // day_high)
else:
    day = 2 + (new_high // day_high)


print(day)