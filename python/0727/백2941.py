word = input()
croa_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
for i in croa_list:
    if i in word:
        word =  word.replace(i, '1')
        



print(len(word))

