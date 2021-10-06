def part(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = part(arr[:mid])
    right_arr = part(arr[mid:])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    global cnt
    left_L = len(left_arr)
    right_L = len(right_arr)
    result = [0]*(left_L+right_L) #하나로 병합 할 것
    left_p, right_p = 0, 0
    i = 0
    if left_arr[-1] > right_arr[-1]: # 병합과정 비교
        cnt += 1

    while left_p < left_L or right_p < right_L:
        if left_p < left_L and right_p < right_L:
            if left_arr[left_p] <= right_arr[right_p]:
                result[i] = left_arr[left_p]
                i += 1
                left_p += 1
            else:
                result[i] = right_arr[right_p]
                i += 1
                right_p += 1
        # 남아있는 것 정렬
        elif left_p < left_L:
            result[i] = left_arr[left_p]
            i += 1
            left_p += 1
        elif right_p < right_L:
            result[i] = right_arr[right_p]
            i += 1
            right_p += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    result = part(arr)

    print(f'#{tc} {result[N//2]} {cnt}')