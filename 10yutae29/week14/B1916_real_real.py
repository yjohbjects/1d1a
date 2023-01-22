# B1916_최소비용 구하기

import heapq

N = int(input())
M = int(input())

# 각 노드별 도착점과 비용을 담을 리스트
# [[], [[2, 2], [3, 3], [4, 1], [5, 10]], [[4, 2]], [[4, 1], [5, 1]], [[5, 3]], []]
road_costs = [[] for _ in range(N+1)]

for m in range(M):
    # s: 시작점, e: 도착점, c: 비용
    s, e, c = map(int, input().split())
    # 도착점과 비용 같이 저장
    road_costs[s].append([c, e])


# 우리가 구하고자 하는 구간 출발점과 도착점의 도시번호
start, end = map(int,input().split())

INF = 10**15
# 시작점부터 각 도시까지 최소비용을 저장할 리스트
start_cost = [INF] * (N+1)
start_cost[start] = 0

# 최소힙에 0(출발지로부터 출발지까지 비용) 과 시작번호 넣어줌
heap = [[0, start]]
heapq.heapify(heap)

#
while heap:
    # 최소힙에서 팝 했으므로
    # cost_from_start가 가장 작은 다음노드를 확인
    cost_from_start, node_num = heapq.heappop(heap)

    if cost_from_start > start_cost[node_num]:
        continue


    for next_info in road_costs[node_num]:
        cost, next_node = next_info
        total_cost = cost_from_start + cost

        if total_cost < start_cost[next_node]:
            start_cost[next_node] = total_cost
            heapq.heappush(heap, [total_cost, next_node])

print(start_cost[end])