from collections import deque
import sys

'''
인풋값만 더 빠르게 받으면 되는 문제
나머지 실행들은 어렵지 않게 구현이 가능
'''

N = int(input())
Q = deque()
for _ in range(N):
    # 인풋값이 한번에 너무 많이 들어올때 유용하게 쓰는 방법!!
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        Q.append(int(order[1]))
    elif order[0] == 'pop':
        if Q:
            print(int(Q.popleft()))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)