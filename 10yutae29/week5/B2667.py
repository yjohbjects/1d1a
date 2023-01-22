# B2667_단지번호붙이기

N = int(input())

apts = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]  # 상하좌우
stack = []
answers = []
for i in range(N):
    for j in range(N):
        if apts[i][j] == 1 and visited[i][j] == 0:
            y = i
            x = j
            visited[y][x] = 1
            stack.append([y,x])
            apt_count = 1
            while stack:
                for d in range(4):
                    ay = y + dy[d]
                    ax = x + dx[d]
                    if 0 <= ay < N and 0 <= ax < N and apts[ay][ax] == 1 and visited[ay][ax] == 0:
                        y = ay
                        x = ax
                        visited[y][x] = 1
                        stack.append([y,x])
                        apt_count += 1
                        break
                else:
                    stack.pop()
                    if len(stack) != 0:
                        y, x = stack[-1]
            answers.append(apt_count)
print(len(answers))
for answer in sorted(answers):
    print(answer)

