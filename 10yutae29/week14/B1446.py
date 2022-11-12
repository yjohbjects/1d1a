# B1446_지름길

# 노드가 아니라 길이로 주어짐
# 다익스트라를 적용하기 위해 거리 1마다 노드 1개로 취급
# 0번 노드부터 D번 노드까지


# N: 지름길의 수, D: 고속도로 길이
N, D = map(int,input().split())

# 지름길의 길이와 지름길 도착점을 저장할 리스트
road_distance = [[] for _ in range(D+1)]

# 각 노드의 지름길 정보를 저장
for _ in range(N):
    from_node, to_node, distance = map(int, input().split())
    # 지름길의 도착지가 고속도로의 길이를 넘어가지 않을때만 저장
    if to_node <= D:
        road_distance[from_node].append([distance, to_node])

# 고속도로 출발점(0번노드)으로 부터 거리를 저장할 리스트
INF = 10**7
distance_from_zero = [INF] * (D+1)
# 출발점 0에서 0번으로 가는 거리는 0으로 초기화
distance_from_zero[0] = 0

# 노드를 탐색
for i in range(D+1):
    # 이전 노드에서 +1 한 값과 기존값 중 작은 값을 저장
    if i:
        distance_from_zero[i] = min(distance_from_zero[i], distance_from_zero[i-1] + 1)
    # 현재 노드에서 지름길이 있을 경우
    # 지름길 도착점의 기존 값과
    # 현재노드 + 지름길 거리 중 작은 값을 저장
    for dis, road in road_distance[i]:
        distance_from_zero[road] = min(distance_from_zero[road], distance_from_zero[i] + dis)

# 도착점까지의 거리 출력
print(distance_from_zero[-1])