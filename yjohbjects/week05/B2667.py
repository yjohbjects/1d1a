def DFS(x, y):
    global house_cnt
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for z in range(4):
        dx = x + dxy[z][0]
        dy = y + dxy[z][1]

        if (0 <= dx < N) and (0 <= dy < N):
            # 집이 있고 방문한 적이 없다면
            if villiage[dx][dy] == '1' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                house_cnt += 1
                DFS(dx, dy)



# 인풋 및 변수 지정
N = int(input())
villiage = [input() for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]
house_cnt = 1
result = []
for i in range(N):
    for j in range(N):
        if villiage[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            DFS(i, j)
            result.append(house_cnt)
            house_cnt = 1

print(len(result))
print(*sorted(result), sep='\n')
