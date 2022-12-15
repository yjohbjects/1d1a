# BAEKJOON 13335 - 트럭 (S1)

'''
문제
1) 강 다리를 n 개의 트럭이 건너감
2) 트럭 순서는 바꿀 수 없으며, 무게는 서로 같지 않음, 다리는 w 대의 트럭만 동시에 이용 가능
3) 다리의 길이는 w 단위길이이며, 각 트럭들은 하나의 단위시간에 하나의 단위길이만큼만 이동
4) 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야함
5) 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성

풀이
1)

입력
1) 입력의 첫 번째 줄에 n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중
2) 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an가 주어지는데, ai는 i번째 트럭의 무게

출력
1) 모든 트럭들이 다리를 건너는 최단시간을 출력
'''
from collections import deque
import sys

sys.stdin = open('B13335.txt')

# input
N, W, L = map(int, input().split())
weights = list(map(int, input().split()))

truck_queue = deque(weights)
bridge = deque([0] * W)
turn = 0

while truck_queue:

    next_truck = truck_queue[0]

    if sum(bridge) + next_truck <= L:
        bridge.popleft()
        truck_queue.popleft()
        bridge.append(next_truck)

    else:
        bridge.popleft()
        if sum(bridge) + next_truck <= L:
            truck_queue.popleft()
            bridge.append(next_truck)
        else:
            bridge.append(0)

    turn += 1

while bridge:
    bridge.popleft()
    turn += 1

# output
print(turn)