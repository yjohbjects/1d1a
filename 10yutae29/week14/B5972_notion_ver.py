
# N:헛간의 개수, # 양방향 길 개수
N, M = map(int, input().split())

# 여물 = 비용(cost)로 산정
# 각 노드별 비용과 목표 노드 저장
road_cost = [[] for _ in range(N+1)]

# 문제에서 양방향 길이라 했으므로 양방향 다 저장
for _ in range(M):
    a, b, cost = map(int, input().split())
    road_cost[a].append([cost, b])
    road_cost[b].append([cost, a])

INF = 10**9

start = 1

distances = [INF] * (N+1)
distances[start] = 0

determined = [0] * (N+1)
determined[start] = 1

for cost, next_node in road_cost[start]:
    distances[next_node] = min(cost, distances[next_node] + cost)
    # distances[next_node] = distance[start] + cost

for _ in range(N):

    min_distance = INF
    min_distance_num = 0

    for next_num in range(N+1):
        if determined[next_num] == 0 and min_distance > distances[next_num]:
            min_distance = distances[next_num]
            min_distance_num = next_num

    determined[min_distance_num] = 1
    for next_cost, next_node in road_cost[min_distance_num]:
        distances[next_node] = min(distances[next_node], distances[min_distance_num] + next_cost)

print(distances[-1])