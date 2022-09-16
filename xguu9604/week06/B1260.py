import sys
sys.stdin = open('input_B1260.txt')

T = int(input())

def DFS(v):
    visited = [False] * (V+1)
    stack = [v]
    answer = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            answer.append(v)
            for w in range(V, 0, -1):
                if arr[v][w] and not visited[w]:
                    stack.append(w)
    return answer

def BFS(v):
    visited = [False] * (V+1)
    Q = [v]
    visited[v] = True
    answer = [v]
    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if arr[v][w] and not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
                answer.append(w)
    return answer


while T > 0:
    V, E, S = map(int, input().split())
    adjs = [list(map(int, input().split())) for _ in range(E)]
    arr = [[False] * (V+1) for _ in range(V+1)]
    for adj in adjs:
        arr[adj[0]][adj[1]] = True
        arr[adj[1]][adj[0]] = True
    dfs = DFS(S)
    bfs = BFS(S)
    for i in range(len(dfs)-1):
        print(dfs[i], end=' ')
    print(dfs[-1])
    for i in range(len(bfs)-1):
        print(bfs[i], end=' ')
    print(bfs[-1])

    T -= 1
