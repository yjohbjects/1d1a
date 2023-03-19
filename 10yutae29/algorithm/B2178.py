# B2178_미로탐색

# BFS

N, M = map(int,input().split())

maze = [input() for _ in range(N)]

# maze의 index가 0부터 시작
n = N-1
m = M-1


q = [[0,0]]

visited = [[0] * M for _ in range(N)]

    # 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    # 현재 위치
    y, x = q.pop(0)

    # 목적지에 도착하면 BFS 종료
    if [y,x] == [N,M]:
        break

    # 델타이동으로 주변 노드로 이동
    for d in range(4):
        n_y = y + dy[d]
        n_x = x + dx[d]
        # 만약 방문하지 않았고, 이동할 수 있는 노드라면 큐에 넣어주고 방문표시
        if 0 <= n_y <N and 0<= n_x <M and visited[n_y][n_x] == 0 and maze[n_y][n_x]=='1':
            q.append([n_y, n_x])
            # 해당 노드까지의 거리를 구해야 하므로 이전 노드의 visited에 +1
            visited[n_y][n_x] = visited[y][x] + 1

print(visited[N-1][M-1] + 1)

