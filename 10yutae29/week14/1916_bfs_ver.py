# B1916_최소비용 구하기

from collections import deque

N = int(input())
M = int(input())

# 각 노드별 도착점과 비용을 담을 리스트
# [[], [[2, 2], [3, 3], [4, 1], [5, 10]], [[4, 2]], [[4, 1], [5, 1]], [[5, 3]], []]
road_cost = [[] for _ in range(N+1)]

for m in range(M):
    # s: 시작점, e: 도착점, c: 비용
    s, e, cost = map(int, input().split())
    # 도착점과 비용 같이 저장
    road_cost[s].append([cost, e])

# 우리가 구하고자 하는 구간 출발점과 도착점의 도시번호
start, end_node = map(int,input().split())

INF = 10**12

# 시작점부터 다른 노드까지의 비용을 저장할 리스트
start_cost = [INF] * (N+1)
start_cost[start] = 0

que = deque([start])

while que:
    now_node = que.popleft()

    for next_cost, next_node in road_cost[now_node]:
        if start_cost[next_node] > start_cost[now_node] + next_cost:
            start_cost[next_node] = start_cost[now_node] + next_cost
            que.append(next_node)

print(start_cost[end_node])
