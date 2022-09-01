T = int(input())

def DFS(x, y):
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 델타이동 (상, 하, 좌, 우)

    for q in range(4):
        dx = x + dxy[q][0]
        dy = y + dxy[q][1]

        # 맵 밖의 위치를 탐색하면 pass
        if dx < 0 or dx >= height or dy < 0 or dy >= width:
            continue
        # 방문한 적 없고, 배추가 있으면 DFS 함수 안으로
        elif visited[dx][dy] == 0 and field[dx][dy] == 1:
            visited[dx][dy] = 1 # 방문도장
            DFS(dx, dy) # 탐색

for t in range(T):

    # input 받기
    width, height, num = map(int, input().split())
    field = [[0] * width for _ in range(height)]

    # 배추 위치 표기
    for p in range(num):
        y, x = map(int, input().split())
        field[x][y] = 1

    # 방문 기록지
    visited = [[0] * width for _ in range(height)]

    cnt = 0
    for i in range(height):
        for j in range(width):
            if field[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] == 1
                DFS(i, j)
                cnt += 1

    print(cnt)
