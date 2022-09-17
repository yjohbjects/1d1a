import sys

N = int(sys.stdin.readline())

stack = []

for test_count in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push' :
        stack.append(command[1])
    elif command[0] == 'pop' :
        if stack :
            print(stack.pop())
        elif not stack :
            print('-1')
    elif command[0] == 'size' :
        print(len(stack))
    elif command[0] == 'empty' :
        if stack :
            print('0')
        elif not stack :
            print('1')     
    elif command[0] == 'top' :
        if stack :
            print(stack[-1])
        elif not stack :
            print('-1')