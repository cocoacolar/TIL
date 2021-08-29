N = int(input())
a = [[] for _ in range(20001)]

for i in range(N):
	word = input()
	k = len(word)
	if word in a[k]:
		pass
	else:
		a[k].append(word)

for i in range(1, 20001):
	if a[i]:
		k = a[i]
		k.sort()
		for x in a[i]:
			print(x)

# import sys    
#
# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     word=[]
#     for i in range(N):
#         word.append(sys.stdin.readline().strip())
#     word = list(set(word))
#     word.sort()
#     word.sort(key=len)
#     for j in word:
#         print(j)