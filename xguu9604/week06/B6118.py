import sys
sys.stdin = open('input_B6118.txt')

from collections import deque

def BFS(v):
    Q = deque([v])
    visited[v] = 1
    while Q:
        v = Q.popleft()
        for w in adjs[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


N, M = map(int, input().split())
adjs = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjs[u].append(v)
    adjs[v].append(u)
visited = [0]*(N+1)
BFS(1)
max_len = 0
cnt = 1
hide = 0
for idx, spot in enumerate(visited):
    if spot > max_len:
        max_len = spot
        cnt = 1
        hide = idx
    elif spot == max_len:
        cnt += 1
print(hide, max_len-1, cnt)
