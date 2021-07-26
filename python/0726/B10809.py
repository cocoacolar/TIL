
word = input()

word_list = 'abcdefghijklmnopqrstuvwxyz'

for spelling in word_list:
    result = word.find(spelling)
    print(result, end=' ')