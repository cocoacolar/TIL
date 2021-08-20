import sys

T = int(input())
stack = []
for tc in range(1, T+1):
    command = sys.stdin.readline().rstrip()
    if command[:4] == 'push':
        x = int(command[4:])
        stack.append(x)
    elif command == 'pop':
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command =='top':
        if stack:
            b = stack.pop()
            print(b)
            stack.append(b)
        else:
            print(-1)