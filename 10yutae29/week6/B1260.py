# B1260_DFS와 BFS

def DFS(dl, n, v):
    visited = [0]*(n+1)
    visited[v] = 1
    stack = [v]
    now = v
    root = [now]
    while stack:
        for ne in dl[now]:
            if visited[ne] == 0:
                stack.append(ne)
                visited[ne] = 1
                now = ne
                root.append(now)
                break
        else:
            stack.pop()
            if len(stack) > 0:
                now = stack[-1]
    return ' '.join(map(str, root))


def BFS(bl, n, v):
    visited = [0] * (n + 1)
    visited[v] = 1
    queue = [v]
    root = []
    while queue:
        now = queue.pop(0)
        root.append(now)
        for ne in bl[now]:
            if visited[ne] == 0:
                visited[ne] = 1
                queue.append(ne)
    return ' '.join(map(str, root))


N, M, V = map(int, input().split())

line = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)
for k in range(1, N+1):
    line[k].sort()

print(DFS(line, N, V))
print(BFS(line, N, V))
