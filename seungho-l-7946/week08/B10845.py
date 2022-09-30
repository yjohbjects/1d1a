# BAEKJOON 10845 - 큐 (S4)

'''
문제
1)

풀이
1)

입력
1)

출력
1)
'''

import sys

sys.stdin = open('B10845.txt')

# input
N = int(sys.stdin.readline())
queue = []
cnt = 0
for i in range(N):
    cmnd1, *cmnd2 = sys.stdin.readline().split()
    if cmnd1 == 'push':
        queue.append(cmnd2[0])
        cnt += 1
    elif cmnd1 == 'pop':
        if queue:
            print(queue[0])
            del queue[0]
            cnt -= 1
        else:
            print(-1)
    elif cmnd1 == 'size':
        print(cnt)
    elif cmnd1 == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmnd1 == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmnd1 == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
