T = int(input())

for tc in range(1, T+1):
    N = int(input())
    zero_arr = [1, 0]
    one_arr = [0, 1]
    if N == 0:
        print(f'{zero_arr[0]} {one_arr[0]}')
    elif N == 1:
        print(f'{zero_arr[1]} {one_arr[1]}')
    else:
        n = 2
        while n < N+1:
            zero_arr.append(zero_arr[n-1]+zero_arr[n-2])
            one_arr.append(one_arr[n - 1] + one_arr[n - 2])
            n += 1
        print(f'{zero_arr[N]} {one_arr[N]}')