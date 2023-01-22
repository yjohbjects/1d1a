# B11725 트리의 부모 찾기

N = int(input())

# 트리 간선정보 저장
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모노드 저장할 리스트
parents = [0]*(N+1)
# BFS를 위한 방문표시 리스트
visited = [0]*(N+1)

# 1번 노드가 루트노드 이므로 1부터 시작
visited[1]=1
q = [1]

# BFS 실행
while q:
    now = q.pop(0)
    for next in tree[now]:
        if not visited[next]:
            q.append(next)
            visited[next] = 1
            # 현재노드가 다음 노드의 부모노드라는 것을 입력
            # 이외에는 기본 BFS와 동일
            parents[next] = now

for parent in parents[2::]:
    print(parent)
