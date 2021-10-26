num_list = list(map(str, input()))
minus = 0
plus = 0
flag = False
p = '0'
m = '0'
for i in num_list:
   
    if (i!='+') and (i!='-') and flag == False:
        p += i
    if (i!='+') and (i!='-') and flag == True:
        m += i
    if i == '-':
        flag = True
        plus += int(p)
        minus += int(m)
        p = '0'
        m = '0'
    elif i == '+':
        plus += int(p)
        minus += int(m)
        p = '0'
        m = '0'
plus += int(p)
minus += int(m)
p = '0'
m = '0'       

k= plus-minus


print(int(k))
