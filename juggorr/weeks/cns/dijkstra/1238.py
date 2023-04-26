import sys
import heapq
sys.stdin = open('in.txt')

N, M, X = map(int, sys.stdin.readline().split())
town = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    town[i][j] = k

# pprint.pprint(town)
# 출발도시에서 X로 가는 길 기록,
# X에서 출발도시로 가는 길 더하기
# 최댓값 출력
# def dijkstra(start, end):
def dijk(start):

    distance = [100 * N * 2 for _ in range(N + 1)]
    distance[start]= 0

    Q = [[0, start]]

    # 시작점에서 END까지 다익스트라로 찾아보기~
    while Q:
        dis, node = heapq.heappop(Q)

        # 힙큐에 (거리, 좌표) 넣기
        for i in range(1, N + 1):
            # 연결되어 있다면
            if town[node][i] != 0:
                # relaxation해야댐
                if distance[i] > dis + town[node][i]:
                    distance[i] = dis + town[node][i]
                    heapq.heappush(Q, [distance[i], i])

    return distance[X]

def dijk_X(start):

    distance = [100 * N * 2 for _ in range(N + 1)]
    distance[start]= 0

    Q = [[0, start]]

    # 시작점에서 END까지 다익스트라로 찾아보기~
    while Q:
        dis, node = heapq.heappop(Q)

        # 힙큐에 (거리, 좌표) 넣기
        for i in range(1, N + 1):
            # 연결되어 있다면
            if town[node][i] != 0:
                # relaxation해야댐
                if distance[i] > dis + town[node][i]:
                    distance[i] = dis + town[node][i]
                    heapq.heappush(Q, [distance[i], i])
    
    return distance

# 1번마을부터 N번 마을까지 X까지 얼마걸리는지 기록하기
result = [0]
for i in range(1, N + 1):
    result.append(dijk(i))

# X마을에서 다른 마을까지 걸리는지 기록하기
result_X = dijk_X(X)

max_time = 0
for i in range(1, N + 1):
    time = result[i] + result_X[i]
    
    if time > max_time:
        max_time = time

print(max_time)