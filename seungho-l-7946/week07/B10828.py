# BAEKJOON 10828 - 스택 (S4)

'''
문제
1) 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성.
2) push, pop, size, empty, top

풀이
1) 구현한다.

입력
1) 첫째 줄에 명령의 수 N, 둘째 줄부터 N개의 줄에는 명령이 1개씩 주어짐.

출력
1) 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력.
'''

import sys

sys.stdin = open('B10828.txt')

# input
stack = []
cnt = 0
top = -1
N = int(sys.stdin.readline())
for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        top = int(order[1])
        stack.append(top)
        cnt += 1
    elif order[0] == 'top':
        print(top)
    elif order[0] == 'size':
        print(cnt)
    elif order[0] == 'empty':
        if cnt == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if cnt == 0:
            top = -1
            print(top)
        else:
            print(stack.pop())
            cnt -= 1
            if cnt == 0:
                top = -1
            else:
                top = stack[-1]
