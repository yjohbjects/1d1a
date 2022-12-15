# B2468 안전 영역


N = int(input())
area = []
height_max = 0
for _ in range(N):
    height = list(map(int,input().split()))
    area.append(height)
    if max(height) > height_max:
        height_max = max(height)

dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]


safe_num = []
for rain in range(1,height_max):
    for i in range(N):
        for j in range(N):
            if area[i][j] <= rain:
                area[i][j] = 0
    visited = [[0]*N for _ in range(N)]
    safe_count = 0
    for i in range(N):
        for j in range(N):
            flag = 0
            if area[i][j] != 0 and visited[i][j]==0:
                y = i
                x = j
                visited[y][x] = 1
                stack = [[y, x]]

            while stack:
                flag = 1
                for d in range(4):
                    ay = y + dy[d]
                    ax = x + dx[d]
                    if 0 <= ay < N and 0 <= ax < N and visited[ay][ax] == 0 and area[ay][ax] != 0:
                        y = ay
                        x = ax
                        stack.append([y, x])
                        visited[y][x] = 1
                        break
                else:
                    stack.pop()
                    if len(stack) > 0:
                        y, x = stack[-1]
            if flag == 1:
                safe_count += 1
    safe_num.append(safe_count)

print(max(safe_num))


