def hanoi(n, o, t, th):
    if n == 1: #
        print(o, th)

    else:
        hanoi(n-1, o, th, t)
        print(o, th)
        hanoi(n-1, t, o, th)




n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)
