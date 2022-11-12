# B5972_택배 배송

import heapq

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

# 시작점은 현서의 헛간 1
start = 1
# 도착점은 찬홍이의 헛간 N
end = N

# 처음에 힙에 [시작점까지비용, 시작점] 을 넣어둠
heap = [[0, start]]
# 최소 힙으로 설정
# 이 힙에서 [비용, 현재 위치]를 삽입, 제거 함
# 그러면 비용이 가장 적은 길부터 계산할 수 있음
heapq.heapify(heap)

# 출발지로부터 비용을 모두 INF로 초기화
INF = 10**15
cost_from_start = [INF]*(N+1)

# 출발지로부터 출발지까지의 비용 = 0
cost_from_start[start] = 0

while heap:
    # 비용과, 현재위치
    cost, now = heapq.heappop(heap)

    # 현재 노드에서 갈 수 있는 노드와 비용 탐색
    for cost_next in road_cost[now]:
        cost_to_next, next_node = cost_next

        # temporary_cost_to_next =
        # 출발지에서 현재 노드까지의 비용 + next_node까지의 비용의 합
        temporary_cost_to_next = cost_from_start[now] + cost_to_next
        # 만약 이 값이 기존의 출발지로부터 next_node까지의 비용보다 작다면
        if temporary_cost_to_next < cost_from_start[next_node]:
            # 출발지로부터 next_node까지의 비용 업데이트
            cost_from_start[next_node] = temporary_cost_to_next
            # 힙에 [ 출발지로부터 next_node까지의 비용, next_node] 저장
            heapq.heappush(heap, [temporary_cost_to_next ,next_node])


print(cost_from_start[-1])
