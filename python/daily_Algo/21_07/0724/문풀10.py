# 10951
# try except 구문을 잘생각하자 , 테스트크 케이스가 정해지지않는 경우

while True:    
    try:    
        x, y = map(int, input().split())
        print(x + y)
    except:
        break
