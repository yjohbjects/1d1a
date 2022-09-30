import sys
sys.stdin = open('in.txt')

from collections import deque
def BFS(v):
    Q = deque([v])
    visited[v] = 1
    while Q:
        v = Q.popleft()
        for w in range(N):
            if maat[v][w] == 'Y' and visited[w] == 0:
                visited[w] = visited[v] + 1
                Q.append(w)

N = int(input())
maat = [list(input()) for _ in range(N)]
maxV = 0
for i in range(N):
    visited = [0] * N
    cnt = 0
    BFS(i)
    for num in visited:
        if num == 2 or num == 3:
            cnt += 1
    if cnt > maxV:
        maxV = cnt
print(maxV)