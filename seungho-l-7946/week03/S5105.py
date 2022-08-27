# SWEA 5105 - 미로의 거리(D3)

'''
NxN 크기의 미로에서 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는 지 알아내는 프로그램을 작성하시오.
경로가 없는 경우 0을 출력한다.

1. 최소/최단거리 문제이므로, BFS 설계
2. Delta를 사용하여 방향 정의
3. 초기 좌표 설정 & 목표 좌표 설정
4. 가능, 불가능 판단하여 가능할 경우, 최단거리 출력
'''

from pprint import pprint
from collections import deque
import sys

sys.stdin = open("S5105.txt")

# 1. BFS 설계
def bfs(x, y, z, k):

    queue = deque() # deque 선언
    queue.append((x, y)) # 출발 좌표 append

    while queue: # queue 안의 원소들이 다 없어질때까지
        print(queue)
        x, y = queue.popleft() # 가장 왼쪽 원소 pop


        for i in range(4): # delta 상하좌우 점검
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: # 테두리 바깥 pass
                continue

            if mat[nx][ny] == 0: # 벽일경우 pass
                continue

            if mat[nx][ny] == 1: # 갈수 있을 경우, 1칸씩 전진하는 것이므로 이동거리 +1 계산
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx, ny)) # 갈수 있으므로, 큐에 append

            if mat[nx][ny] == 3: # 목적지 도착의 경우
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx, ny))

    return mat[z][k] - 3 # 3값이 목적지이므로 3을 빼주도록 함

# 2. Delta를 사용하여 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전체 케이스 input
num = int(input())

for tc in range(1, num + 1):

    # input
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    # 3. 초기 좌표 설정 & 목표 좌표 설정
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                sx, sy = i, j

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 3:
                ex, ey = i, j

    # 0과 1 switch - 좀 더 직관적으로 생각하기 위함
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                mat[i][j] = 0
            elif mat[i][j] == 0:
                mat[i][j] = 1

    # pprint(mat)
    # output
    result = bfs(sx, sy, ex, ey)
    print(f'#{tc} {result}')