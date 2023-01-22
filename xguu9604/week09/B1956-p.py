import sys
sys.stdin = open('input_B1956.txt')

'''
Dijkstra를 통한 최단 경로의 싸이클을 찾기
분명히 엣지 케이스가 있다고 생각했고 틀릴것이라 생각했는데 맞음..
그런데 알고보니 그것은 엣지가 아니였구연
'''

from collections import deque

# 싸이클을 돌 수 있는 조깅 루트를 찾아보자
def jogging(s):
    global distance
    global can_run
    # 해당 지점까지의 달리기 거리를 기록
    visited = [0] * (V+1)
    # 큐생성
    Q = deque()
    Q.append(s)
    # 전부 순회 합시다
    while Q:
        u = Q.popleft()
        # 만약 지금 기록된 거리가 최소 싸이클 거리보다 길다면 패스
        if visited[u] > distance:
            continue
        # 출발지로 돌아왔고 방문 기록지에 값이 있다면 한바퀴 돌고 왔다는 의미
        if u == s and visited[u]:
            # 값에 현재 달린 거리와 기록값 사이에 최솟값으로 갱신
            distance = min(distance, visited[u])
            # 여기까지 왔다면 싸이클이 있다는 것이므로 달리기 가능에 체크
            can_run = 1
        # 출발지가 아닌경우에는 BFS
        else:
            for v in range(1, V+1):
                # 아직 가본적 없는 곳이며 현재 지점과 연결되어있다면 가보자!
                if not visited[v] and adj_lst[u][v]:
                    Q.append(v)
                    visited[v] = visited[u] + adj_lst[u][v]
                # 한번 가본적이 있고 연결되어있는 곳일때
                elif visited[v] and adj_lst[u][v]:
                    # 거기까지 가는데 기록된 거리가 지금 지점에서 가는 기댓값보다 크다면
                    if visited[v] > visited[u] + adj_lst[u][v]:
                        # 그 쪽으로 가면서
                        Q.append(v)
                        # 그 지점까지 가는 최소 거리를 지금 루트로 갱신
                        visited[v] = visited[u] + adj_lst[u][v]


V, E = map(int, input().split())
adj_lst = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_lst[n1][n2] = w
# 싸이클 거리의 최솟값을 받아줄 변수
distance = 10000*V
# 조깅이 가능한지를 나타내줄 변수
can_run = 0
# 모든 노드를 시작점으로 조깅 판단
for i in range(1, V+1):
    jogging(i)
# 조깅을 끝냈다면 최소 거리를
if can_run:
    print(distance)
# 조깅을 할 수 없다면 -1 출력
else:
    print(-1)