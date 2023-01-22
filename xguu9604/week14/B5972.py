import sys
from collections import deque


'''
다익이에서 착안했던 BFS 코드입니다
이게 3번에는 안먹히는게 좀 화가 나네요
'''


# 가지치기 해주고 최소비용으로 계산하는 BFS 함수 정의
def BFS(s, g):
    # 정답은 전역변수로 계속 최신화 해줌
    global answer
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        # 현재 보고 있는 그 친구의 경로 값이 현재 답보다 큰 값이라면
        # 가망성이 없는 노드! 건너뛰자
        if visited[u] > answer:
            continue

        # 현재 보고 있는 노드가 목적지라면
        if u == g:
            # 지금까지 계산한 비용과 정답 값중 최솟값을 정답에 기록
            answer = min(visited[u], answer)


        # 아직 목적지에 도달 못했으면
        else:
            # 연결 상태를 확인하자
            for info in routes[u]:
                to = info[0]
                cost = info[1]
                # 만약 현재 가는 곳을 아직 가본적이 없으면
                if not visited[to]:
                    # 해당 노드를 일단 추가해주자
                    Q.append(to)
                    # 그리고 그 노드에 가는 비용을 기록
                    visited[to] = visited[u] + cost
                # 아니면 기록은 되어있는데 현재 기댓값보다 큰 값이 적혀있다면
                elif visited[to] > visited[u] + cost:
                    # 그 노드를 다시 추가해주고
                    Q.append(to)
                    # 최솟값으로 최신화
                    visited[to] = visited[u] + cost



N, M = map(int, sys.stdin.readline().split())
routes = [[] for _ in range(N+1)]
for _ in range(M):
    s, g, cost = map(int, sys.stdin.readline().split())
    routes[s].append([g, cost])
    routes[g].append([s, cost])
visited = [0] * (N+1)
answer = 1000 * N
BFS(1, N)
print(answer)