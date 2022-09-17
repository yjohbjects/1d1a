import sys
from collections import deque


# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:

        target = queue.popleft()

        # 연결된 헛간을 확인
        for i in graph[target]:
            # 방문하지 않은 헛간이라면 방문
            if visited[i] == 0:
                # 방문 거리를 체크
                visited[i] = visited[target] + 1
                queue.append(i)


n, m = map(int, sys.stdin.readline().split())

# 노드 방문 여부와 순서 확인
visited = [0 for i in range(n + 1)]

# 각 연결된 노드를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 헛간부터 탐색
bfs(1)

# 최대 값의 인덱스 값 출력, 첫번째 헛간을 1로 두었기 때문에 최대값에서 1을 빼준 값을 출력, 최대 값의 개수 출력
print(visited.index(max(visited)), max(visited) - 1, visited.count(max(visited)))