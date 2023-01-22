# B10845_큐

import sys
N = int(input())
q = []
for _ in range(N):
    info = list(sys.stdin.readline().split())
    if info[0] == 'push':
        q.append(info[1])
    elif info[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif info[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif info[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif info[0] == 'size':
        print(len(q))
    elif info[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)