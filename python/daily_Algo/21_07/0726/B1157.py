

word = input().upper()

Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = []
for i in Alpha:
    word_num = word.count(i)
    result.append(word_num)
high_score = 0
anws = ''


if 2 <= result.count(max(result)):
    print('?')
else:
    for i in range(26):
        if high_score < result[i]:
            high_score = result[i]
            anws = Alpha[i]

print(anws)
        