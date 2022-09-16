import sys
sys.stdin = open('input_B2583.txt')
from pprint import pprint

def is_in(i, j):
    if 0 <= i < M and 0 <= j < N:
        return True
    return False

def BFS(i, j):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    stack = [[i, j]]
    if arr[stack[0][0]][stack[0][1]] or visited[stack[0][0]][stack[0][1]]:
        return 0
    areas.append(0)
    while stack:
        current = stack.pop()
        if not visited[current[0]][current[1]]:
            visited[current[0]][current[1]] = True
            areas[-1] += 1
            for dir in dirs:
                ni = current[0] + dir[0]
                nj = current[1] + dir[1]
                if is_in(ni, nj) and not arr[ni][nj] and not visited[ni][nj]:
                    stack.append([ni, nj])
    return 1


M, N, K = map(int, input().split())
rectangles = [list(map(int, input().split())) for _ in range(K)]
# print(rectangles)
arr = [[False] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
areas = []
for rectangle in rectangles:
    for j in range(rectangle[0], rectangle[2]):
        for i in range(rectangle[1], rectangle[3]):
            arr[M-i-1][j] = True
section = 0
for i in range(M):
    for j in range(N):
        section += BFS(i, j)
areas = sorted(areas)
print(section)
for i in range(len(areas)-1):
    print(areas[i], end=' ')
print(areas[-1])
