import sys
from collections import deque


'''
이 문제는 하나의 개념만 알면 어렵지 않은 문제
트리에서의 지름은 임의의 한점에서 제일 먼 점을 찾고
그 점으로 부터 제일 먼 점까지의 거리가 지름이다
'''


# 임의의 점으로 부터 각 점들까지의 거리들을 구하는 함수
def BFS(n):
    Q = deque()
    Q.append(n)
    distances[n] = 0
    while Q:
        v = Q.popleft()
        for info in adjLst[v]:
            w = info[0]
            weight = info[1]
            if distances[w] == -1:
                Q.append(w)
                distances[w] = distances[v] + weight


N = int(input())
adjLst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, weight = map(int, sys.stdin.readline().split())
    adjLst[a].append([b, weight])
    adjLst[b].append([a, weight])
# 각 노드까지의 거리들을 구해주는 기록지
distances = [-1] * (N + 1)
# 루트에서 각 노드까지의 거리를 구하자
BFS(1)
# 루트에서 가장 먼 노드 번호 찾기
max_distance = 0
max_idx = 0
for idx, distance in enumerate(distances):
    if distance > max_distance:
        max_idx = idx
        max_distance = distance
# 기록지를 다시 초기화 해주고
distances = [-1] * (N + 1)
# 가장 먼 노드를 찾아주자
BFS(max_idx)
print(max(distances))