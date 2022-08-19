# 5102_그래프 경로

from queue import deque
import sys

sys.stdin = open("input.txt")

def BFS(x, y, count, visited):

    queue = deque()
    queue.append(x)

    while queue:
        w = queue.popleft()
        for i in graph[w]:
            if visited[i] == 0:
                count[i] = count[w] + 1
                queue.append(i)
                visited[i] = 1

    return count[y]

T = int(input())

for tc in range(1, T+1):

    # input
    V, E = map(int, input().split())

    # graph
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    # history
    visited = [0] * (V+1)

    # objective
    S, G = map(int, input().split())
    cnt = [0] * (V+1)

    # output
    result = BFS(S, G, cnt, visited)
    print(f'#{tc} {result}')