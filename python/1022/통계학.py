import sys
from collections import Counter
n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(int(sys.stdin.readline()))
s.sort()

print(round(sum(s)/n))

print(s[n//2])

c = Counter(s).most_common()
if len(s) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

print(s[-1] - s[0])