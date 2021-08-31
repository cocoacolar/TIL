x, y = map(int, input().split())
a,b = x, y
maxV = 0
minV = 0
h = min(a, b)
for i in range(1, h+1):
	if a%i == 0 and b%i == 0:
		maxV = i
k = 1
minV = maxV * k
while minV % a != 0 or minV % b != 0:
	k += 1
	minV = maxV * k
print(maxV)
print(minV)

# 방법 2
a, b = x, y
while b:
    a,b = b, a%b

gcd = a

lcm = (x*y)//gcd

print(gcd, lcm)

