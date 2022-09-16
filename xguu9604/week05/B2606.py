import sys
sys.stdin = open('input_B2606.txt')

def DFS(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for w in range(2, N+1):
                if adjlst[v][w] == True and visited[w] == False:
                    stack.append(w)
    return

N = int(input())
E = int(input())
connects = [list(map(int, input().split())) for _ in range(E)]
adjlst = [[False]*(N+1) for _ in range(N+1)]
for connect in connects:
    adjlst[connect[0]][connect[1]] = True
    adjlst[connect[1]][connect[0]] = True

visited = [False]*(N+1)

DFS(1)
cnt = 0
for visit in visited:
    if visit == True:
        cnt += 1
print(cnt-1)