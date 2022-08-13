# S4875 미로

T = int(input())
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]  # 상하좌우

for t in range(T):
    maze_size = int(input())
    maze = [list(map(int, input())) for _ in range(maze_size)]
    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 3:
                x = j
                y = i
                x_idx = 0
                y_idx = 0
    while True:
        if (y-1 >= 0 and (maze[y-1][x] == 0 or maze[y-1][x] == 2)):
            x_idx = 0
            y_idx = 0
        elif (y+1 < maze_size and (maze[y+1][x] == 0 or maze[y+1][x] == 2)):
            x_idx = 1
            y_idx = 1
        elif (x-1 >= 0 and (maze[y][x-1] == 0 or maze[y][x-1] == 2)):
            x_idx = 2
            y_idx = 2
        elif (x+1 < maze_size and (maze[y][x+1] == 0 or maze[y][x+1] == 2)):
            x_idx = 3
            y_idx = 3
        elif (
                (y-1 < 0 or maze[y-1][x] == 1)
                and (y+1 >= maze_size or maze[y+1][x] == 1)
                and (x-1 < 0 or maze[y][x-1] == 1)
                and (x+1 >= maze_size or maze[y][x+1] == 1)
        ):
            print(f'#{t+1} 0')
            break



        maze[y][x] = 1
        x = x + dx[x_idx]
        y = y + dy[y_idx]
        if maze[y][x] == 2:
            print(f'#{t+1} 1')
            break

