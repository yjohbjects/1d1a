# 입력 변수 받기
N, M, V = map(int,input().split())

# 인접 0 행렬 생성
matrix = [[0]*(N+1) for i in range(N+1)]

# 방문한 곳 체크 배열
visited = [0] * (N+1)

# 입력 받는 두 값에 대해 0행렬 1삽입
for i in range(M):
    a, b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V) :
    visited[V] = 1
    print(V, end = ' ')

    for i in range(1, N+1) :
        if visited[i]==0 and matrix[V][i] == 1 :
            dfs(i)

# 이제 bfs 차례
def bfs(V) :
    queue = [V]

    visited[V] = 0

    # 큐가 비워질 때까지
    while queue :
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if visited[i] == 1 and matrix[V][i] == 1 :
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)