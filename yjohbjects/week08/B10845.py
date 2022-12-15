# B10845 큐

import sys
N = int(input())
command = [sys.stdin.readline().strip() for x in range(N)]
queue = []

for i in range(N):

    # push X: 정수 X를 스택에 넣는 연산이다.
    if command[i][:4] == 'push':
        a, b = map(str, command[i].split())
        queue.append(int(b))

    # size: 스택에 들어있는 정수의 개수를 출력한다.
    elif command[i] == 'size':
        print(len(queue))

    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif command[i] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # pop, top 명령이지만 stack이 빈 경우
    elif len(queue) == 0:
        print(-1)

    else:
        # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if command[i] == 'pop':
            print(queue.pop(0))

        # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif command[i] == 'front':
            print(queue[0])
        # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif command[i] == 'back':
            print(queue[-1])