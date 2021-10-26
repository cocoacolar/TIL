N = int(input())
num = list(map(int, input().split()))
M = int(input())
ans = list(map(int, input().split()))

num.sort()

for x in ans:
    left = 0
    end = N-1
    center = (left + end)//2
    while True:
        if (end-left == 1):
            if num[end]==x or num[left]==x:
                print(1)
                break
            else:
                print(0)
                break
        
    
        if num[center] == x:
            print(1)
            break
        elif num[center] < x:
            left = center
            center = (left + end)//2
        elif num[center] > x:
            end = center
            center = (left + end)//2
