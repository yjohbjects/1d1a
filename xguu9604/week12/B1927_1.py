import heapq
import sys

'''
힙 모듈을 받아서 사용해봤읍니다.
'''


N = int(input())
# 힙을 선언해줍니다
heap = []
for _ in range(N):
    # 인풋을 int(input())으로 받으면 런타임 에러가 나더군요
    # 그래서 더 빠른 친구로 받아봤어요
    num = int(sys.stdin.readline())
    # 0이면 연산을 진행
    if num == 0:
        # 비어있으면 0 출력
        if heap == []:
            print(0)
        # 원소가 있다면 최솟값 출력
        else:
            print(heapq.heappop(heap))
    # 그 외의 경우에는 힙 순서에 맞게 그 숫자 넣어주기
    else:
        heapq.heappush(heap, num)