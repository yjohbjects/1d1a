def DFS(v):
    stack = [v]

    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
        
            for w in range(1, C + 1):
                if mat[v][w] == 1:
                    stack.append(w)

C = int(input())
R = int(input())
mat = [[0] * (C + 1) for _ in range(C + 1)]
visited = [0] * (C + 1)

for _ in range(R):
    r, c = map(int, input().split())
    mat[r][c] = 1
    mat[c][r] = 1

DFS(1)
print(sum(visited) - 1)