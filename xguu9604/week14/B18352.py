import sys
from collections import deque


'''
다익이 맞아요?
그냥 BFS로 쓱 풀어벌임
'''


# 길찾기 함수
# 평소 BFS와 똑같이 진행하지만 가지치기 조건만 하나 추가
def BFS(n):
    Q = deque()
    Q.append(n)
    visited[n] = 1
    while Q:
        v = Q.popleft()
        # 만약 현재 보고 있는 노드가 갈길이 더 멀어지는 순간 함수 종료
        if visited[v] > K:
            return
        for w in adjLst[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


N, M, K, X = map(int, sys.stdin.readline().split())
adjLst = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
routes = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjLst[a].append(b)
BFS(X)
# 방문 기록지 보면서 원하는 최소 길이를 가지는 노드 찾아서 기록
for i in range(1, N+1):
    if visited[i] == K+1:
        routes.append(i)
# 길이 하나라도 기록되있으면 노드 출력
if routes:
    for route in routes:
        print(route)
# 없으면 -1
else:
    print(-1)