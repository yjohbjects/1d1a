import sys
sys.stdin = open('B2644.txt')
from pprint import pprint
from collections import deque

def BFS(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for w in range(1, N + 1):
            if mat[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1   

N = int(input())
s, e = map(int, input().split())
M = int(input())
mat = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    r, c = map(int, input().split())
    mat[r][c] = 1
    mat[c][r] = 1

BFS(s)
print(visited[e] - 1)