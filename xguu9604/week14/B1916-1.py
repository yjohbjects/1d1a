import sys


def Dijkstra(s):
    max_val = 100000 * N
    weights = [max_val] * (N+1)
    weights[s] = 0
    visited = [0] * (N + 1)

    for _ in range(N):
        minIdx = -1
        min_val = max_val
        for i in range(1, N+1):
            if not visited[i] and weights[i] < min_val:
                min_val = weights[i]
                minIdx = i
        visited[minIdx] = 1

        for w in range(1, N+1):
            if not visited[w] and weights[minIdx] + cities[minIdx][w] < weights[w] and cities[minIdx][w]:
                weights[w] = weights[minIdx] + cities[minIdx][w]

    return weights


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
max_val = 100000 * N
cities = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, g, cost = map(int, sys.stdin.readline().split())
    cities[s][g] = cost

A, B = map(int, sys.stdin.readline().split())
D = [0] * (N+1)
answer = Dijkstra(A)

print(answer[B])