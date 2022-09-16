import sys
sys.stdin = open('input_B2644.txt')

# BFS 함수 정의
def BFS(v):
    Q = [v]
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1, N+1):
            if w == end and adjfamily[v][w] == True:
                return visited[v]
            elif adjfamily[v][w] == True and not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    return -1

T = 2
while T > 0:
    N = int(input())
    start, end = map(int, input().split())
    E = int(input())
    family = [list(map(int, input().split())) for _ in range(E)]
    adjfamily = [[False] * (N+1) for _ in range(N+1)]
    for fam in family:
        adjfamily[fam[0]][fam[1]] = True
        adjfamily[fam[1]][fam[0]] = True
    visited = [0]*(N+1)
    answer = BFS(start)
    print(answer)
    T -= 1