# B1987_알파벳

R, C = map(int,input().split())

alphas = [list(input()) for _ in range(R)]

answer = 0

y, x = 0, 0

visited = [[0]*C for _ in range(R)]
visited[0][0] = 1

stack = [[y,x, 0]]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

inserted_set = set()
inserted_set.add(alphas[0][0])

num = 0

while stack:
    y, x, k= stack.pop()
    for d in range(k,4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < R and 0 <= nx <C and alphas[ny][nx] not in inserted_set and visited[ny][nx] == 0:
            stack.append([y, x, d + 1])
            stack.append([ny, nx, 0])
            inserted_set.add(alphas[ny][nx])
            visited[ny][nx] = 1
            num += 1
            break
    else:
        inserted_set.remove(alphas[y][x])
        visited[y][x] = 0
        answer = max(answer,num)
        num -= 1

print(answer + 1)