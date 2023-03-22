n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0  # 그림의 개수
max_area = 0  # 가장 큰 그림의 넓이

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:  # 색칠된 부분을 찾으면
            count += 1  # 그림의 개수를 증가시키고
            area = 1  # 그림의 넓이를 1로 초기화하고

            queue = [(i, j)]  # BFS를 위한 큐에 시작점을 추가
            picture[i][j] = 0  # 방문한 지점은 0으로 처리

            while queue:
                x, y = queue.pop(0)  # 큐에서 하나의 지점을 꺼내서
                for k in range(4):  # 상하좌우 네 방향으로 탐색
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1:
                        queue.append((nx, ny))  # 큐에 방문하지 않은 인접한 지점을 추가
                        picture[nx][ny] = 0  # 방문한 지점은 0으로 처리
                        area += 1  # 그림의 넓이를 1 증가시킴
            
            max_area = max(max_area, area)  # 그림의 넓이의 최대값을 계산

print(count)
print(max_area)
