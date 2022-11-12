import sys
from collections import deque


def BFS(s):
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for info in cities[u]:
            to = info[0]
            cost = info[1]
            if not costs[to]:
                Q.append(to)
                costs[to] = costs[u] + cost
            elif costs[to] > costs[u] + cost:
                Q.append(to)
                costs[to] = costs[u] + cost


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
cities = [[] for _ in range(N+1)]
for _ in range(M):
    s, g, cost = map(int, sys.stdin.readline().split())
    cities[s].append([g, cost])
A, B = map(int, sys.stdin.readline().split())
costs = [0] * (N+1)
BFS(A)
print(costs)
print(costs[B])
