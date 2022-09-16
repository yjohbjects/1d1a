import sys
sys.stdin = open('input_B2644.txt')

def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, N+1):
                if arr[v][w] == 1 and visited[w]:
                    relate[v] = relate[w] + 1
                elif v == start:
                    relate[start] = 1
                if arr[v][w] == 1 and not visited[w]:
                    stack.append(w)


T = int(input())
while T > 0:
    N = int(input())
    start, end = map(int, input().split())
    M = int(input())
    relations = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    relate = [0] * (N+1)
    for relation in relations:
        arr[relation[0]][relation[1]] = 1
        arr[relation[1]][relation[0]] = 1
    dfs(start)
    print(relate[end]-1)
    T -= 1
