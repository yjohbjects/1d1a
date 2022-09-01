# B2644 촌수계산

def DFS(x):
    global cnt, result
    visited[x] = 1
    for j in links[x]:
        if visited[j] != 1: # 방문하지 않았다면
            cnt += 1
            if j == P2:
                result = cnt
            DFS(j)

ppl_num = int(input())
P1, P2 = map(int, input().split())
N = int(input())
links = [[] for _ in range(ppl_num + 1)]
visited = [0] * (ppl_num + 1)

cnt = 0
result = -1
for i in range(N):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

DFS(P1)
print(result)
