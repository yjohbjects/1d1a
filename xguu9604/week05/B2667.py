import sys
sys.stdin = open('input_B2667.txt')

def is_in(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def DFS(i, j):
    if not arr[i][j] or visited[i][j]:
        return 0
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    stack = [[i, j]]
    cnt = 0
    while stack:
        current = stack.pop()
        if not visited[current[0]][current[1]]:
            visited[current[0]][current[1]] = 1
            cnt += 1
            for dir in dirs:
                ni = current[0] + dir[0]
                nj = current[1] + dir[1]
                if is_in(ni, nj) and arr[ni][nj] and not visited[ni][nj]:
                    stack.append([ni, nj])
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
home_lst = []
for i in range(N):
    for j in range(N):
        homes = 0
        homes = DFS(i, j)
        if homes:
            home_lst.append(homes)
home_lst = sorted(home_lst)
print(len(home_lst))
for homes in home_lst:
    print(homes)