#B1743_음식물 피하기

N, M, K = map(int,input().split())

floor = [[0]*(M+1) for _ in range(N+1)]

for _ in range(K):
    y, x = map(int,input().split())
    floor[y][x] = 1


visited = [[False]*(M+1) for _ in range(N+1)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0

for i in range(1,N+1):
    for j in range(1,M+1):
        if floor[i][j] == 1 and visited[i][j] == False:
            stack=[[i,j]]
            visited[i][j] = True
            cnt = 1
            while stack:
                y, x = stack[-1]
                for d in range(4):
                    n_y = y + dy[d]
                    n_x = x + dx[d]
                    if 0<n_x<=M and 0<n_y<=N and visited[n_y][n_x] == False and floor[n_y][n_x] == 1:
                        stack.append([n_y,n_x])
                        visited[n_y][n_x] = True
                        cnt+=1
                        break
                else:
                    stack.pop()
            ans = max([cnt,ans])
print(ans)