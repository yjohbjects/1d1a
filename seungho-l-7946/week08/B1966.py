# BAEKJOON 1966 - 프린터 큐 (S3)

'''
문제
1) 프린터기는 다음과 같은 조건에 따라 인쇄
2) 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
3) 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
4) 그렇지 않다면 바로 인쇄

풀이
1) enumerate 사용
2) list 2개 사용

입력
1) 첫 줄에 테스트케이스의 수
2) 첫 번째 줄에는 문서의 개수 N과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
3) 맨 왼쪽은 0번째, 두 번째 줄에는 N개 문서의 중요도가 차례대로

출력
1) 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄
'''
from collections import deque
import sys

sys.stdin = open('B1966.txt')

T = int(input())

for tc in range(T):

    # input
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    queue = deque(num_list)
    idx_queue = deque([i for i in range(N)])

    # pointer
    result = 0
    idx = 0
    while queue:
        if idx in idx_queue:
            if queue[0] == max(queue):
                num_pop = queue.popleft()
                idx_pop = idx_queue.popleft()
                result += 1
                if num_pop == num_list[M] and idx_pop == M:
                    break
            else:
                queue.rotate(-1)
                idx_queue.rotate(-1)
        idx += 1
        idx %= N

    # output
    print(result)