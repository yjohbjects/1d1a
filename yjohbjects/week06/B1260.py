# B1260 DFS와 BFS

def DFS(n):
    print(n, end=' ')
    visited[n] = 1
    for node in graph[n]:
        if visited[node] == 0:
            DFS(node)


def BFS(n):
    visited = [0 for _ in range(N + 1)]
    visited[n] = 1
    queue = [n]
    while queue:
        pin = queue.pop(0)
        print(pin, end=' ')
        for node in graph[pin]: # [2, 3, 4]
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)] # [[], [2, 3, 4], [4], [4], []]
visited = [0 for _ in range(N + 1)]  # [0, 0, 0, 0, 0]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(len(graph)):
    graph[j] = sorted(graph[j])
    # print(g)

DFS(V)
print()
BFS(V)
