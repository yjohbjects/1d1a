import sys

def Dijkstra(n):
    global max_val
    U = [0] * (N+1)
    U[n] = 1
    for w in range(1, N+1):
        D[w] = cities[n][w]

    for _ in range(N-1):
        min_val = max_val
        w = 0
        for i in range(1, N+1):
            if not U[i] and min_val > D[i]:
                min_val = D[i]
                w = i
        U[w] = 1

        for v in range(1, N+1):
            if cities[w][v]:
                D[v] = min(D[v], D[w] + cities[w][v])


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
max_val = 100000 * N
cities = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, g, cost = map(int, sys.stdin.readline().split())
    if cities[s][g]:
        cities[s][g] = min(cost, cities[s][g])
    else:
        cities[s][g] = cost

A, B = map(int, sys.stdin.readline().split())
D = [0] * (N+1)
Dijkstra(A)
print(D)