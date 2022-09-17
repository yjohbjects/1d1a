import sys
sys.stdin = open('input_B10828.txt')
from collections import deque
T = int(input())

while T > 0:
    N = int(input())
    stack = deque()
    for _ in range(N):
        # 반복문으로 여러줄의 인풋을 받을때에 input()을 사용하면 시간초과가 발생할 수 있음
        # 그런 경우에는 sys.stdin.readline()을 사용하면 시간 초과를 방지할 수 있다..!
        orders = sys.stdin.readline().split()
        order = orders[0]
        if order == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif order == 'size':
            print(len(stack))
        elif order == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif order == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        else:
            stack.append(orders[1])

    T -= 1
