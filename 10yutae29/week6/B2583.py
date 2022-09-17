# B2583_영역구하기

M, N, K = map(int,input().split())
box = [[0]*N for _ in range(M)]

for _ in range(K):
    info = list(map(int, input().split()))
    xs = info[0]
    ys = M - info[3]
    xe = info[2]
    ye = M - info[1]
    for y in range(ys, ye):
        for x in range(xs, xe):
            box[y][x] = 1
answer = []
visited = [[0]*N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for y in range(M):
    for x in range(N):
        if box[y][x] == 0 and visited[y][x] == 0:
            # 여기서 bfs 시작
            queue = [[y, x]]
            visited[y][x] = 1
            b_count = 1
            while queue:
                y, x = queue.pop(0)
                for d in range(4):
                    ay = y + dy[d]
                    ax = x + dx[d]
                    if 0 <= ay < M and 0 <= ax < N and box[ay][ax]==0 and visited[ay][ax]==0:
                        visited[ay][ax] = 1
                        queue.append([ay, ax])
                        b_count += 1
            answer.append(b_count)
print(len(answer))
print(' '.join(map(str,sorted(answer))))


