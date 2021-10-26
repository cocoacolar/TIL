dial_str = input()



dial_dict = {
'2': 'ABC', '3': 'DEF', '4': 'GHI', 
'5': 'JKL', '6': 'MNO', '7': 'PQRS',
'8': 'TUV', '9': 'WXYZ'   
}

result = 0
for k in dial_str:
    for key in dial_dict:
        if k in dial_dict[key]:
            result += int(key)+1
        else:
            continue

print(result)


