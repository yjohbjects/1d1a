# B2164 카드2

'''
한 싸이클 :
맨 위 카드 제거하고
맨위 카드를 제일 아래로 추가

* pop(0)는 시간초과.. deque로 풀어야함
'''

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    # 맨 위 카드 제거
    queue.popleft()
    # 맨 위 카드를 제일 아래로
    queue.append(queue.popleft())

print(queue.popleft())