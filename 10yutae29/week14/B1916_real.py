# B1916_최소비용 구하기

N = int(input())
M = int(input())

# 각 노드별 도착점과 비용을 담을 리스트
# [[], [[2, 2], [3, 3], [4, 1], [5, 10]], [[4, 2]], [[4, 1], [5, 1]], [[5, 3]], []]
road_costs = [[] for _ in range(N+1)]

for m in range(M):
    # s: 시작점, e: 도착점, c: 비용
    s, e, c = map(int, input().split())
    # 도착점과 비용 같이 저장
    road_costs[s].append([e, c])


# 우리가 구하고자 하는 구간 출발점과 도착점의 도시번호
start, end = map(int,input().split())

INF = 10**15
# 시작점부터 각 도시까지 최소비용을 저장할 리스트
start_cost = [INF] * (N+1)
start_cost[start] = 0

fixed = [0] * (N+1)
fixed[start] = 1
for next_city, next_cost in road_costs[start]:
    start_cost[next_city] = next_cost

for _ in range(N):
    min_value = INF
    t = 0

    for i in range(N+1):
        if fixed[i] == 0 and min_value > start_cost[i]:
            min_value = start_cost[i]
            t = i
    fixed[t] = 1
    for next_city, next_cost in road_costs[t]:
        start_cost[next_city] = min(start_cost[next_city], start_cost[t] + next_cost)

print(start_cost[end])