# B2606 바이러스

def DFS(x):
    global cnt
    visited[x] = 1
    for j in links[x]:
        if visited[j] != 1: # 방문하지 않았다면
            DFS(j)
            cnt += 1

com_num = int(input())
pair_num = int(input())

links = [[] for _ in range(com_num+1)]
visited = [0] * (com_num + 1)

cnt = 0
for i in range(pair_num):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

# 1 입력
DFS(1)
print(cnt)
