# P72413_합승 택시 요금

# 다익스트라를 활용하여 출발점에서 모든 노드까지의 거리
# a 도착점에서 모든 노드까지의 거리
# b 도착점에서 모든 노드까지의 거리 를 구할거임
# (출발점 ~ 분기점) + (분기점 ~ a 도착점) + (분기점 ~ b도착점) 을 구하여 최소값을 찾을것

# 평범한 다익스트라
# start로부터 각 노드로 가는 최소비용이 담긴 리스트를 return
def djikstra(road_costs:list, n:int, start:list):
    INF = 10**12

    taxi_cost = [INF] * (n+1)
    taxi_cost[start] = 0

    determined = [0] * (n+1)

    determined[start] = 1

    for cost, next_node in road_costs[start]:
        taxi_cost[next_node] = min(cost, taxi_cost[next_node])

    for _ in range(n):

        min_cost = INF
        min_cost_num = 0

        for next_num in range(n+1):
            if determined[next_num] == 0 and min_cost > taxi_cost[next_num]:
                min_cost = taxi_cost[next_num]
                min_cost_num = next_num

        determined[min_cost_num] = 1

        for next_cost, next_node in road_costs[min_cost_num]:
            taxi_cost[next_node] = min(taxi_cost[next_node], taxi_cost[min_cost_num] + next_cost)

    return taxi_cost

def solution(n, s, a, b, fares):
    answer = 10**15

    # 각 노드별 도착점과 비용을 담을 리스트
    road_costs = [[] for _ in range(n+1)]

    for fare in fares:
        # from, to, cost
        f, t, c = fare
        road_costs[f].append([c, t])
        road_costs[t].append([c, f])

    # 시작점, a점, b점에서 모든 지점까지의 최소 거리를
    # 다익스트라를 통해 리스트로 구함
    start_branch = djikstra(road_costs,n, s)
    branch_to_a = djikstra(road_costs,n, a)
    branch_to_b = djikstra(road_costs,n, b)
    #[1000000000000, 10, 66, 51, 0, 34, 35]
    #[1000000000000, 25, 48, 26, 35, 2, 0]
    #[1000000000000, 63, 0, 22, 66, 46, 48]

    # 각 리스트의 같은 인덱스 비용을 합하면 택시 이용요금이 나옴
    # start_branch[i] 는 시작점으로부터 분기점 i까지 가는데 드는 비용(a, b 같이 택시타는 비용)
    # branch_to_a[i]는 분기점 i에서 a도착점 가지 가는 비용(a혼자 가는 비용)
    # branch_to_b[i]는 분기점 i에서 b도착점 가지 가는 비용(b혼자 가는 비용)
    # 이중 가장 작은 비용을 answer로 출력
    for i in range(1,n+1):
        taxi_cost = start_branch[i] + branch_to_a[i] + branch_to_b[i]
        if taxi_cost < answer:
            answer = taxi_cost

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))