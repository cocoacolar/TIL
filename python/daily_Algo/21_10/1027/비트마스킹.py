# 2진수 표현
switch = 0b1001100011
print(switch)
'''
>>> 611
'''
binary = bin(611)
print(binary)
'''
0b1001100011
'''

# 비트 연산
# AND 연산 &
print(bin(0b1000000000 & 0b1))

#OR 연산 |
print(bin(0b1111 | 0b0001))

# XOR 연산 ^
print(bin(0b1111 ^ 0b1001))

# Shift 연산 <<
print(bin(~0b0010 <<2))
n = 3
print(bin(0b1010 & ~(1 << n)))  #  0b10