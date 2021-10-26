
# 더 간단한 풀이 존재

senten = input()
if senten == ' ':
    print(0)
else:
    result = senten.strip()

    ans = result.count(' ')

    print(ans+1)
    

