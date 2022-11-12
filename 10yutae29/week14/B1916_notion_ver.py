# B1916_최소비용 구하기

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


# 노드의 최소 비용이 정해졌음을 표시하는 리스트 (like visited)
determined = [0] * (N+1)
# 출발 노드 방문 표시
determined[start] = 1
# 출발 노드에서 연결된 다음노드까지의 비용 계산
for cost, next_node in road_cost[start]:
    start_cost[next_node] = min(cost, start_cost[next_node])
    # distances[next_node] = distance[start] + cost

# 출발노드 제외한 다른 노드들 거리 계산
for _ in range(N):

    # 현재 출발지로부터 최저비용이 안정해진 노드중 비용이 가장 작은 노드의 비용
    min_cost = INF
    # 가장 작은 노드의 비용을 가진 노드 번호
    min_cost_num = 0

    # 노드를 순회하면서 확인함
    for next_num in range(N+1):
        # 만약 그 출발점으로부터 그 노드까지의 최저비용이 정해지지 않았고,
        # min_distance보다 그 노드까지의 비용이 작다면
        if determined[next_num] == 0 and min_cost > start_cost[next_num]:
            # 최소 비용 = next_num노드까지의 비용
            min_cost = start_cost[next_num]
            # 최소 비용을 가진 노드 = next_num
            min_cost_num = next_num

    # 정해진 min_cost_num 노드 결정 표시
    determined[min_cost_num] = 1

    # 그 노드에서 갈 수 있는 노드의 최소거리 구함
    for next_cost, next_node in road_cost[min_cost_num]:
        start_cost[next_node] = min(start_cost[next_node], start_cost[min_cost_num] + next_cost)

print(start_cost[end_node])