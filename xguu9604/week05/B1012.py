import sys
sys.stdin = open('input_B1012.txt')

def is_in(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def DFS(i, j):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    stack = [[i, j]]
    if visited[stack[-1][0]][stack[-1][1]] or not field[stack[-1][0]][stack[-1][1]]:
        return 0
    while stack:
        current = stack.pop()
        if not visited[current[0]][current[1]]:
            visited[current[0]][current[1]] = 1
            for dir in dirs:
                nx = current[0] + dir[0]
                ny = current[1] + dir[1]
                if is_in(nx, ny) and not visited[nx][ny] and field[nx][ny]:
                    stack.append([nx, ny])
    return 1

T = int(input())
while T > 0:
    M, N, vegi = map(int, input().split())
    spots = [list(map(int, input().split())) for _ in range(vegi)]
    field = [[0]*M for _ in range(N)]
    for spot in spots:
        field[spot[1]][spot[0]] = 1
    visited = [[0]*M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            answer += DFS(i, j)
    print(answer)
    T -= 1