# atoi ,itoa


def atoi(s):
    i = 0
    if s[0] == '-':

    elif s[0] == '+':

    else:
        for x in s:
            i = i*10 + ord(x)-ord('0')
        return i

def itoa(i):
    s = ''
    while i>0:
        chr(i%10 + ord('0'))

    return s
#

