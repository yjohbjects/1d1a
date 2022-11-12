# B18352_특정 거리의 도시 찾기

from collections import deque

# N : 도시의 개수, M : 도로의 개수
# K : 거리 정보(목표 최단 거리), X : 출발 도시의 번호
N, M, K, X = map(int,input().split())

# 각 도시에서 갈 수 있는 도시번호
# [[], [2, 3], [3, 4], []]
next_cities = [[] for _ in range(N+1)]
for _ in range(M):
    f, t = map(int,input().split())
    next_cities[f].append(t)

INF = 10**9

# 출발지점 X로부터 다른 도시까지의 거리

x_distance = [INF] * (N+1)

# 출발점에서 줄발점까지는 거리 0
x_distance[X] = 0

# BFS로 도시를 탐방하기 위해 큐 만들어줌
que = deque([X])

# 거리가 전부 1이라 한번 방문했을 때 거리가 최소거리가 됨
visited = [0]*(N+1)

while que:
    # 현재 위치
    now = que.popleft()

    # 현재 위치에서 갈 수 있는 도시들까지의 거리를 계산할 거임
    for next_city in next_cities[now]:
        # 만약 방문하지 않았다면 거리 계산
        if not visited[next_city]:
            # 다음 방문을 위해 큐에 다음도시 번호 입력
            que.append(next_city)
            # 다음 도시로의 거리는 현재 도시에서 거리+1을 한 값과 이전에 있던 거리의 값의 최소
            # 여기선 INF와 현재 도시에서 거리+1을 한 값을 비교
            x_distance[next_city] = min(x_distance[next_city], x_distance[now] + 1)
            # 방문 표시
            visited[next_city] = 1

# X로부터 거리가 K인 도시의 번호를 리스트로 받음
k_nums = []
for idx in range(N+1):
    if x_distance[idx] == K:
        k_nums.append(idx)

# 만약 K거리인 도시가 있다면 순차적 출력
if k_nums:
    for k_num in k_nums:
        print(k_num)
# 없다면 -1 출력
else:
    print(-1)