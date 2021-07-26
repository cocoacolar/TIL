# 1 <= N <= 1000

#한수 갯수구하는 함수 만들기



def han(a):
    
    count = 0
    if a  <= 99:
        return a
    else:
        for i in range(100, a+1):
            num =  str(i)
            
            if (int(num[0]) - int(num[1])) == (int(num[1]) - (int(num[2]))):
                count += 1     
        return 99 + count


T = int(input())

print(han(T))

