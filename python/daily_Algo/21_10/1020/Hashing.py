

def change(words):
	ans = 0
	r = 31
	for i in range(len(words)):
		num = ord(words[i])-96
		ans += (num*r**i)
	M = 1234567891
	ans = ans%M
	return ans
N = int(input())
words = input()
print(change(words))
