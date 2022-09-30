# BAEKJOON 2164 - 카드 2 (S4)

'''
문제
1) 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태. 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
2) 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김

풀이
1)

입력
1)

출력
1)
'''
from collections import deque
import sys

sys.stdin = open('B2164.txt')

# input
N = int(input())
queue = deque([i + 1 for i in range(N)])

# while len(queue) != 1:
#     queue.popleft()
#     queue.rotate(-1)

result = 0
while queue:

    if len(queue) == 1:
        result = queue[0]
        break

    queue.popleft()
    queue.rotate(-1)

# result = queue[0]

# output
print(result)