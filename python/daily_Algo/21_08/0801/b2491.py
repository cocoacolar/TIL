T = int(input())

num_list = list(map(int, input().split()))
result_up = 1
result_down = 1
result_list = [2]

if num_list.count(num_list[0]) != len(num_list):
    for i in range(T-1):
        if num_list[i] < num_list[i+1]:
            result_down = 1
            result_up += 1
            result_list.append(result_up)
        elif  num_list[i] > num_list[i+1]:
            result_up = 1
            result_down += 1
            result_list.append(result_down)
        else:
            result_up += 1
            result_down += 1
            result_list.append(result_up)
            result_list.append(result_down)
    if max(result_list) <= 2:
        print(2)
    else:
        print(max(result_list))
else:
    print(len(num_list))